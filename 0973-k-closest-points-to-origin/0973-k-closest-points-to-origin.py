# max heap of length k

from heapq import heappop, heappush

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        def find_dist(x1, y1, x2, y2):
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

        heap = []

        for x, y in points:
            dis = find_dist(x, y, 0, 0)

            if len(heap) < k:
                heappush(heap, (-dis, x, y))
            elif -heap[0][0] > dis:
                heappop(heap)
                heappush(heap, (-dis, x, y))

        return [[x, y] for _, x, y in heap]
