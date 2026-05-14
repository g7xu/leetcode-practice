# visited set
# res
# BFS on the cities

from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()

        for i in range(len(isConnected)):
            if i in visited:
                continue
            
            res += 1
            queue = deque([i])
            visited.add(i)
            while queue:
                cur = queue.popleft()

                for ne in range(len(isConnected[cur])):
                    if isConnected[cur][ne] == 1 and ne not in visited:
                        queue.append(ne)
                        visited.add(ne)

        return res



        