# minHepa of sell
# maxHeap for buy

from heapq import heappop, heappush

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        minHeapSell = [] # price, amount
        maxHeapBuy = []

        for p, a, o in orders:
            if o == 0:
                # processing
                while minHeapSell and minHeapSell[0][0] <= p and a != 0:
                    if minHeapSell[0][1] <= a:
                        _, tmp = heappop(minHeapSell)
                        a -= tmp
                    else:
                        minHeapSell[0][1] -= a
                        a = 0
                if a:
                    heappush(maxHeapBuy, [-p, a])
                        
            else:
                while maxHeapBuy and -maxHeapBuy[0][0] >= p and a != 0:
                    if maxHeapBuy[0][1] <= a:
                        _, tmp = heappop(maxHeapBuy)
                        a -= tmp
                    else:
                        maxHeapBuy[0][1] -= a
                        a = 0
                if a:
                    heappush(minHeapSell, [p, a])

        res = 0
        for _, re in maxHeapBuy:
            res += re

        for _, re in minHeapSell:
            res += re

        return res % (10**9 + 7)


        # return len(maxHeapBuy) + len(minHeapSell)

