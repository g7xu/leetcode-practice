# DFS with back tracking

# x, y, visited, 

# check if x, y is the bottom right

# check down or right,

# if going out or visited

# return number of possible path from current point to the final

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x = y = 0
        
        @cache
        def helper(x, y):
            if x == m - 1 and y == n - 1:
                return 1

            p = 0
            for dx, dy in [(0, 1), (1, 0)]:
                nx = dx + x
                ny = dy + y

                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    p += helper(nx, ny)
            
            return p

        return helper(0, 0)