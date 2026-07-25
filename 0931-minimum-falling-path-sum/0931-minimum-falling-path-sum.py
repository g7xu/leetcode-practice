# idea
# dp problem bottom up
# O(n)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix) 
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[n - 1][i] = matrix[n-1][i]

        for i in range(n - 2, -1, -1):
            for j in range(n):
                
                can = []
                for m in [-1, 0, 1]:
                    can_j = j + m

                    if can_j >= 0 and can_j < n:
                        can.append(dp[i+1][can_j])

            
                dp[i][j] = matrix[i][j] + min(can)

        return min(dp[0])

