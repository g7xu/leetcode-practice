from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandQueue = deque(sandwiches)
        queue = deque(students)
        while queue:
            original_len = len(queue)
            for _ in range(len(queue)):
                cur = queue.popleft()
                # print(cur, sandQueue[0])
                if cur == sandQueue[0]:
                    sandQueue.popleft()
                else:
                    queue.append(cur)

            if len(queue) == original_len:
                return original_len

        return 0
