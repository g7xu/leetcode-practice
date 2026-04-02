# BFS

# find rotten organge
# find fresh orange

# queue

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))



        t = 0
        while queue:
            if fresh == 0:
                return t

            t += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx = x + dx
                    ny = y + dy

                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]) and grid[nx][ny] == 1:
                        fresh -= 1
                        grid[nx][ny] = 2
                        queue.append((nx, ny))


                
        if fresh == 0:
            return t
            
        return -1

        
