# bfs on all the cells=

from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        visited = set()
        
        def bfs(x, y, grid, visited, k):
            queue = deque([(x, y)])
            visited.add((x, y))
            total = grid[x][y]

            while queue:
                x, y = queue.popleft()
                
                for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nx = x + dx
                    ny = y + dy

                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]) and (nx, ny) not in visited and grid[nx][ny] > 0:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        total += grid[nx][ny]

            # print(total)
            return total % k == 0
                        


        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] > 0:
                    res += bfs(i, j, grid, visited, k)

        return res


        