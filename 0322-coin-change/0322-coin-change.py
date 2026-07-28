
# [....]


# compare to the previous one
# 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1) 
        coins.sort()
        
        for i in range(1, len(dp)):
            can = []
            for coin in coins:
                if coin > i:
                    break
                
                if dp[i - coin] >= 0:
                    can.append(1 + dp[i - coin])

            if can:
                dp[i] = min(can)
            else:
                dp[i] = -1

        return dp[-1]
                
        