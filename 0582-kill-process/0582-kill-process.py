# 变种的tree traverse

# BFS with effective mapping

from collections import defaultdict, deque

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent = defaultdict(set)

        for c, p in zip(pid, ppid):
            parent[p].add(c)

        queue = deque([kill])
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            
            for c in parent[cur]:
                queue.append(c)

        return res


        