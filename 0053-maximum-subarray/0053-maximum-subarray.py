# classic sliding window

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        fast = 0
        cur = 0
        while fast < len(nums):
            if cur < 0 and nums[fast] > cur:
                cur = 0

            cur += nums[fast]
            res = max(res, cur)
            fast += 1

        return res