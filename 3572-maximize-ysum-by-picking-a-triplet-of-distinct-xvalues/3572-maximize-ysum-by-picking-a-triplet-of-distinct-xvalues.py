# heap to track the best three
# dict to track group

from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        group = defaultdict(lambda: float('-inf'))
        
        
        for g_id, num in zip(x, y):
            group[g_id] = max(group[g_id], num)
            

        Minheap = []
        for val in group.values():
            if len(Minheap) < 3:
                heappush(Minheap, val)
            elif Minheap[0] < val:
                heappop(Minheap)
                heappush(Minheap, val)

        return -1 if len(Minheap) < 3 else sum(Minheap)


