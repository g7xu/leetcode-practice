r""" Thinking area
res = -1

hastable manage -> sub-em list

BFS

queue (i-th, time)
- update the res
- push its subs into the queue
- 


"""

from collections import deque, defaultdict

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        manageDict = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            manageDict[manager[i]].append(i)
        

        queue = deque([(headID, 0)])
        res = 0
        while queue:
            m_id, timeTaken = queue.popleft()

            res = max(res, timeTaken)

            for sub_id in manageDict[m_id]:
                queue.append((sub_id, timeTaken + informTime[m_id]))

        return res