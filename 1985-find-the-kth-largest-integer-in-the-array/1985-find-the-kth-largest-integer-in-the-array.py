from heapq import heapify, heappush, heappop

class Num:
    def __init__(self, s):
        self.s = s

    def __lt__(self, other):
        if len(self.s) != len(other.s):
            return len(self.s) < len(other.s)
        
        return int(self.s) < int(other.s)

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minHeap = []
        
        for num in nums:
            heappush(minHeap, Num(num))
            if len(minHeap) > k:
                heappop(minHeap)

        return minHeap[0].s