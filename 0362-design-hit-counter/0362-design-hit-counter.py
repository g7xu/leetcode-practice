from heapq import heappop, heappush

class HitCounter:

    def __init__(self):
        self.minheap = []
        
    def hit(self, timestamp: int) -> None:
        heappush(self.minheap, timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.minheap and self.minheap[0] <= timestamp - 300:
            heappop(self.minheap)

        return len(self.minheap)

        
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)