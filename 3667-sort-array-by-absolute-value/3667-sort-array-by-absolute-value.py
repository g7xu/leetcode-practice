from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        

        minheap = []
        absDict = defaultdict(list)

        # construct dict, heap
        for ele in nums:
            if ele > 0:
                absDict[abs(ele)].append(ele)
            else:
                absDict[abs(ele)].insert(0, ele) # 

            if len(absDict[abs(ele)]) == 1:
                heappush(minheap, abs(ele))

        # construct the sorted array
        res = []
        while minheap:
            cur = heappop(minheap)
            res = res + absDict[cur]

        return res



# print(absSort([2, -7, -2, -2, 0]))