# BFS
# 

from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:        
        queue = deque([[0, 0]])
        visited = set((0, 0))
        step = 0
        while queue:
            for _ in range(len(queue)):
                cx, cy = queue.popleft()

                if cx == x and cy == y:
                    return step
                
                
                for dx, dy in [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2], [2, 1], [2, -1]]:
                    nx = dx + cx
                    ny = dy + cy

                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append([nx, ny])

            step += 1

                

