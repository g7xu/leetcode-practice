# start time: 2:36
# end time: ~

# thinking: 2:36 - 2:46
# writing: ~
# end: ~

# give up at the end

# spend 30 mins

from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visited = set()
        minHeap = [(0, 0)]

        def cal_dis(p1, p2):
            return (
                abs(p1[0] - p2[0]) + 
                abs(p1[1] - p2[1])
            )

        while len(visited) != len(points):
            new_c, new_p = heappop(minHeap)

            if new_p in visited:
                continue

            visited.add(new_p)
            res += new_c

            for i in range(len(points)):
                if i in visited:
                    continue

                heappush(minHeap, (cal_dis(points[new_p], points[i]), i))

        return res
