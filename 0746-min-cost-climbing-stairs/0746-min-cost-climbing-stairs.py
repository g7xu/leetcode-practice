class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 1:
            return 0
        
        dp = [0] * (len(cost) + 1) 

        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        for i in range(len(dp) - 3, -1, -1):
            if i == 0:
                dp[i] = min(dp[i + 1], dp[i + 2])
            else:
                dp[i] = cost[i - 1] + min(dp[i + 1], dp[i + 2])

        return dp[0]


