# dfs
# backtracking

# counter = visited empty square
# once reach the ending check if counter == empty square counts,
# if yes return 1

# dfs(x, y, counter)
# if x, y is the ending, checking and return

# try four direction and move
# recurisve called
# backtracking

# return result

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # find empty sqaure
        empty_square = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty_square += 1
                elif grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 2:
                    tx, ty = i, j


        visited = set()
        def helper(x, y, c):
            if x == tx and y == ty:
                if c == empty_square:
                    return 1
                else:
                    return 0

            res = 0
            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                nx = x + dx
                ny = y + dy

                print(nx, ny, n, m)
                if nx >= 0 and nx < m and ny >= 0 and ny < n and (nx, ny) not in visited and (grid[nx][ny] == 0 or grid[nx][ny] == 2):
                    c += 1
                    visited.add((nx, ny))
                    res += helper(nx, ny, c)
                    visited.remove((nx, ny))
                    c -= 1

            return res

        return helper(x, y, 0)


