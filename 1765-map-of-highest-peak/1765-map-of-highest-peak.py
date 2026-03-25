# multiple Source BFS

# however, when colliding, check the difference if more than 1, reduce that height

# from heapq import heappush, heappop
# class Solution:
#     def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
#         visited = set()
#         res = []

#         heap = []
#         for i in range(len(isWater)):
#             level = []
#             for j in range(len(isWater[i])):
                
#                 if isWater[i][j]:
#                     level.append(0)
#                     visited.add((i, j))
#                     heappush(heap, (0, i, j))
#                     continue

#                 level.append(-1)
#             res.append(level)

#         while heap:
#             h, i, j = heappop(heap)

#             for id, jd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                 ni = i + id
#                 nj = j + jd

#                 if ni >= 0 and ni < len(res) and nj >= 0 and nj < len(res[ni]) and (ni, nj) not in visited:
#                     res[ni][nj] = res[i][j] + 1
#                     heappush(heap, (res[ni][nj], ni, nj))
#                     visited.add((ni, nj))

#         return res


# from heapq import heappush, heappop
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        visited = set()
        res = []

        queue = deque([])
        for i in range(len(isWater)):
            level = []
            for j in range(len(isWater[i])):
                
                if isWater[i][j]:
                    level.append(0)
                    visited.add((i, j))
                    queue.append((0, i, j))
                    continue

                level.append(-1)
            res.append(level)

        while queue:
            h, i, j = queue.popleft()

            for id, jd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + id
                nj = j + jd

                if ni >= 0 and ni < len(res) and nj >= 0 and nj < len(res[ni]) and (ni, nj) not in visited:
                    res[ni][nj] = res[i][j] + 1
                    queue.append((res[ni][nj], ni, nj))
                    visited.add((ni, nj))

        return res


            

