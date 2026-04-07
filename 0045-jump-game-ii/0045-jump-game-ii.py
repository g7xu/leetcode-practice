# DP - bottom up

"""
[2, 1, 2, 1, 0]

[2, 3, 1, 1, 0]


# is current step reachable to the final, if yes, 1
# if not, check all the possible position, find the minimum + 1
"""



class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)


        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1
                continue

            lowest = float('inf')
            for p in range(i + 1, min(len(nums), i + nums[i] + 1)):
                lowest = min(dp[p], lowest)

            dp[i] = 1 + lowest

        return dp[0]