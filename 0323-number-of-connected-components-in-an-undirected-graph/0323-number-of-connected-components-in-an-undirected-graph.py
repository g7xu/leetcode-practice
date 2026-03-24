# BFS or DFS would solve the problem, will use BFS here

# logic
#1 creating the mapping dict
#2 dfs on every node, increase count with 1 each time perform BFS, if already visited
#then don't perform BFS

from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping = defaultdict(list)

        for a, b in edges:
            mapping[a].append(b)
            mapping[b].append(a)

    
        
        def bfs(node, visited):
            queue = deque([node])

            while queue:
                cur = queue.popleft()
                visited.add(cur)
                
                for ne in mapping[cur]:
                    if ne not in visited:
                        queue.append(ne)

        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                bfs(i, visited)

        return res




        