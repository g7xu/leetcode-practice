from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []

        for stone in stones:
            heappush(maxheap, -stone)

        while len(maxheap) > 1:
            x = heappop(maxheap)
            y = heappop(maxheap)

            remain = x - y

            if x != 0:
                heappush(maxheap, remain)

        if maxheap:
            return -maxheap[0]
        else:
            return 0