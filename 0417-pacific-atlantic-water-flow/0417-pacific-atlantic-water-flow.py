# we think the problem this way, from the each side
# clinbing up and mark the cell with with the side by doing BFS
# all the mark with the shared color with the added



from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        p_fill = [[0 for _ in range(n)] for _ in range(m)]
        a_fill = [[0 for _ in range(n)] for _ in range(m)]

        def bfs(fill, queue):
            while queue:
                x, y = queue.popleft()
                fill[x][y] = 1

                for m_x, m_y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nx = m_x + x
                    ny = m_y + y

                    if nx >= 0 and nx < m and ny >= 0 and ny < n and fill[nx][ny] != 1 and heights[nx][ny] >= heights[x][y]:
                        fill[nx][ny] = 1
                        queue.append((nx, ny))


        # the pacific ocean
        queue = deque([])
        
        # left
        for i in range(m):
            queue.append((i, 0))
        # right
        for j in range(n):
            queue.append((0, j))

        bfs(p_fill, queue)

        # the altantic ocean
        queue = deque([])

        for i in range(m):
            queue.append((i, n - 1))

        for j in range(n):
            queue.append((m - 1, j))

        bfs(a_fill, queue)


        res = []
        for i in range(m):
            for j in range(n):
                if a_fill[i][j] + p_fill[i][j] == 2:
                    res.append([i, j])

        
        return res 

        





            

