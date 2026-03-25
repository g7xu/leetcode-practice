# when I see a 1, do BFS to count the island size, 

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        grid = [[y for y in x] for x in grid]
        res = 0

        def helper(x, y, grid):
            print(x, y)
            size = 0
            Queue = deque([(x, y)])

            while Queue:
                x, y = Queue.popleft()
                
                if grid[x][y] == 0:
                    continue
                
                size += 1
                grid[x][y] = 0
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx = x + dx
                    ny = y + dy

                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]) and grid[nx][ny] == 1:
                        Queue.append((nx, ny))

            print(size)
            return size

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, helper(i, j, grid))

        return res

        