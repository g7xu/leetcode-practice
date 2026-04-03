from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_count = defaultdict(int)
        next_course = defaultdict(list)

        for a, b in prerequisites:
            pre_count[a] += 1
            next_course[b].append(a)

        Queue = deque([i for i in range(numCourses) if pre_count[i] == 0])

        taken = []
        while Queue:
            course = Queue.popleft()
            taken.append(course)
            for nc in next_course[course]:
                pre_count[nc] -= 1
                if pre_count[nc] == 0:
                    Queue.append(nc)

        if len(taken) != numCourses:
            return []

        return taken


        