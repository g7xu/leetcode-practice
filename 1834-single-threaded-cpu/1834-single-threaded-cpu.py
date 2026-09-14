r""" Thinking area


heap, processTime, index, and enqueTime

heap with enqueueTime

current_time

while enque heap:
    pop until > currentime

    if still empty, fast foward time and add the top one

    process and update result

"""

from heapq import heappush, heappop, heapify

class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """

        sorted_tasks = sorted([[i, tasks[i][0], tasks[i][1]] for i in range(len(tasks))], key = lambda x: x[1])

        print(sorted_tasks)

        MinHeap = []
        res = []
        p = 0
        currTime = 0
        while p < len(sorted_tasks):
            if not MinHeap and currTime < sorted_tasks[p][1]:
                currTime = sorted_tasks[p][1]

            while p < len(sorted_tasks) and sorted_tasks[p][1] <= currTime:
                heappush(MinHeap, [sorted_tasks[p][2], sorted_tasks[p][0]])
                p += 1

            ptime, i = heappop(MinHeap)
            res.append(i)
            currTime += ptime

        while MinHeap:
            ptime, i = heappop(MinHeap)
            res.append(i)
            currTime += ptime

        return res
            


        