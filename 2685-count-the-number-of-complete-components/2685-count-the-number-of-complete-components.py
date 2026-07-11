# find compoents

# know the unique edges
# 

from collections import deque, defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        print(adj)
        
        def dfs(node, arr):
            queue = deque([node])
            visited.add(node)

            while queue:
                cur = queue.popleft()
                arr.append(cur)
                for ne in adj[cur]:
                    if ne not in visited:
                        queue.append(ne)
                        visited.add(ne)

            return arr



        res = 0 
        visited = set()
        for i in range(n):
            if i in visited:
                continue
        
            components = dfs(i, [])
            if all([len(adj[c]) == len(components) - 1 for c in components]):
                res += 1

        return res
