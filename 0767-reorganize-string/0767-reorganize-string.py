# tackle this problem with priority queue

from heapq import heappop, heappush, heapify
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        res = ''

        # creating max heap
        heap = [[-v, k] for k, v in Counter(s).items()]
        heapify(heap)

        # print(heap)
        # return 

        while heap:
            if len(heap) == 1:
                freq, k = heappop(heap)
                freq = -freq

                if res and res[-1] == k:
                    return ''

                res = res + k

                if freq - 1 != 0:
                    heappush(heap, [-(freq - 1), k])

                continue

            freq1, k1 = heappop(heap)
            freq1 = -freq1
            freq2, k2 = heappop(heap)
            freq2 = -freq2

            res = res + k1 + k2

            if freq1 - 1 != 0:
                heappush(heap, [-(freq1 - 1), k1])

            if freq2 - 1 != 0:
                heappush(heap, [-(freq2 - 1), k2])

        return res





        
        