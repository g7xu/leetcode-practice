class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        task_coolDown = dict()
        d = 0
        for task in tasks:
            if task in task_coolDown and task_coolDown[task] > d:
                d = task_coolDown[task]
                task_coolDown[task] = d + space + 1
                continue

            d += 1
            task_coolDown[task] = d + space + 1
            # print(d)
            # print(task_coolDown)

        return d



        