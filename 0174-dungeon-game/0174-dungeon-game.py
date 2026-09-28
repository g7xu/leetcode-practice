# Looking for path with max minimum value

# try all the path, track the minimum value of all the path, min(0, max(...))

# top down

# minimumn health required to reach this block, their corresponding status

# (3, 1) (6, 1) (6, 4)
# (8, 1) 
# (8, 11) 


# 0 0 0
# 0 0 -5
# 0 0 -5

class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [[None for _ in range(n)] for _ in range(m)]

        # inital state
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])

        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = max(1, dp[m - 1][i + 1] - dungeon[m - 1][i])

        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(
                    1,
                    min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                )

        return dp[0][0]