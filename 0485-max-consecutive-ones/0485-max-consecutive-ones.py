class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = right = 0
        res = 0

        while right < len(nums):

            while right < len(nums) and nums[right] == 1:
                right += 1

            res = max(res, right - left)
            right += 1
            left = right

        return res