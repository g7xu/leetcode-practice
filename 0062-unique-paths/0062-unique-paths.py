# DFS with back tracking

# x, y, visited, 

# check if x, y is the bottom right

# check down or right,

# if going out or visited

# return number of possible path from current point to the final

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # row
        for i in range(m):
            dp[i][0] = 1

        # col
        for j in range(n):
            dp[0][j] = 1

        # top down
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j-1]

        return dp[m - 1][n - 1]