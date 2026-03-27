# logic 
# minHeap of length k, convert nums to int

from heapq import heappop, heappush

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        minheap = []

        for num in nums:
            num = int(num)

            if len(minheap) < k:
                heappush(minheap, num)
            elif minheap[0] < num:
                heappush(minheap, num)
                heappop(minheap)

        return str(minheap[0])
