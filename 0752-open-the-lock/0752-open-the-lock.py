from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(['0000'])
        deadends = set(deadends)

        queue = deque(['0000'])

        res = 0
        while queue:

            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur in deadends:
                    continue

                if cur == target:
                    return res

                for i in range(len(cur)):
                    for j in [1, -1]:
                        change = int(cur[i]) + j
                        if change == 10:
                            change = 0
                        
                        if change == -1:
                            change = 9

                        new = cur[:i] + str(change) + cur[i + 1:]

                        if new in visited:
                            continue

                        visited.add(new)
                        queue.append(new)

            res += 1

        return -1



                        
