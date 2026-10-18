"""
# dfs

# helper 

# input
## x
## y
## n
## visited
## result


if n == 0:
    res += 1
    return

# all possible loc

# filter out invalid location
# market visted
# func call
# backtrack

"""

class Solution:
    def knightDialer(self, n: int) -> int:
        grid = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["*", "0", "#"],
        ]
        
        @cache
        def helper(x, y, n):
            if n == 0:
                return 1

            res = 0
            for xm, ym in [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]:
                nx = x + xm
                ny = y + ym

                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]) and grid[nx][ny] not in ["*", "#"]:
                    res += helper(nx, ny, n - 1)

            return res
            
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in ["*", "#"]:
                    continue

                res += helper(i, j, n - 1)

        return res % (10**9 + 7)