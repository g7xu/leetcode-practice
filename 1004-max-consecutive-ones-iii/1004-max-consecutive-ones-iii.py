# sliding window?


# moving forward when
# is 1, or is zero but have k left

# reduce when f is zero and k is 0

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        original = nums[::]

        s = f = 0
        res = 0
        while f < len(nums):
            if nums[f] == 0:
                k -= 1

            while k < 0:
                if nums[s] == 0:
                    k += 1
                
                s += 1

            res = max(res, f - s + 1)
            f += 1

        return res


