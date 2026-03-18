# visit all node BFS?
# priority queue with BFS?

# everytime treverse a new edge, find the earliest endtime

from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # hashmap creation
        mapping = defaultdict(list)

        for u, v, w in times:
            mapping[u].append((v, w))

        print(mapping)

        visited = set()
        heap = [[0, k]] # [endtime, target queue]

        res = 0
        while heap:
            if len(visited) == n:
                return res

            endtime, node = heappop(heap)
            res = max(res, endtime)
            visited.add(node)

            for v, w in mapping[node]:
                if v not in visited:
                    heappush(heap, [endtime + w, v])

        if len(visited) == n:
            return res

        return -1

            







            
