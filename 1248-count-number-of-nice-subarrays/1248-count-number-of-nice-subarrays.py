class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = right = 0
        curr_odd = 0

        res = 0

        @cache
        def count_sub(l, r):
            if l == r:
                return 1

            if nums[l] % 2 == 1:
                return 1

            return 1 + count_sub(l + 1, r)


        while right < len(nums):
            
            if nums[right] % 2 == 1:
                curr_odd += 1

            while curr_odd > k:
                if nums[left] % 2 == 1:
                    curr_odd -= 1
                left += 1

            if curr_odd == k:
                res += count_sub(left, right)

            right += 1

        return res


                