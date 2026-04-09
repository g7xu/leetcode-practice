from heapq import heappop, heappush, heapify
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = [-1 * num for num in nums]

        heapify(maxHeap)

        res = 0
        for _ in range(k):
            val = -1 * heappop(maxHeap)

            res += val

            val = math.ceil(val / 3)

            heappush(maxHeap, -1 * val)

        return res


        
        