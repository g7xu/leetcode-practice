# BFS with multiple source

# queue with BFS
# 

from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        queue = deque([])
        INF = 2 ** 31 - 1

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        while queue:
            for _ in range(len(queue)):
                cr, cc = queue.popleft()

                for mr, mc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nr = mr + cr
                    nc = mc + cc

                    if nr >= 0 and nr < m and nc >= 0 and nc < n and rooms[nr][nc] == INF:
                        rooms[nr][nc] = rooms[cr][cc] + 1
                        queue.append((nr, nc))

        return 