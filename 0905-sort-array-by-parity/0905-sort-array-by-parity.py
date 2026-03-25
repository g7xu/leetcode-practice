# two pointer

# [3, 1, 2, 4]

# []
# [1] while l < r
# [1, 2]


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        l = 0
        r = len(nums) - 1
        while l < r:

            # find odd
            while l < len(nums) and nums[l] % 2 == 0:
                l += 1

            while r >= 0 and nums[r] % 2 == 1:
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]

        return nums


