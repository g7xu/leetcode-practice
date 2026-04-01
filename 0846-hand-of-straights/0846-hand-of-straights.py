from heapq import heappop, heappush, heapify

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        minHeap = [[k, v] for k, v in Counter(hand).items()]

        heapify(minHeap)
        print(minHeap)

        while minHeap:
            remains = []
            s = None
            for _ in range(groupSize):
                if not minHeap:
                    return False 
                num, freq = heappop(minHeap)
                if freq > 1:
                    remains.append([num, freq - 1])

                if s is None:
                    s = num
                else:
                    if num - 1 != s:
                        print(num, s)
                        return False
                    else:
                        s = num
                
            for remain in remains:

                heappush(minHeap, remain)

        return True
                    


