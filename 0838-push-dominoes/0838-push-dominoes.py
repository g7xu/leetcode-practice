# BFS

# .L.R...LR..L..

# 1 sec
# LL.RR.LLRRLL..

# 2 sec
# LL.RR.LLRRLL..

# BFS 
# with a queue 
# ele: [(idx, dir)]

# process the queu by round/sec
# when colid set back to .
# 

from collections import deque, defaultdict

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        queue = deque([])
        dominoes = list(dominoes)
        for idx in range(len(dominoes)):
            if dominoes[idx] != '.':
                if dominoes[idx] == 'L':
                    queue.append((idx - 1, 'L'))
                else:
                    queue.append((idx + 1, 'R'))
            
        while queue:
            to_change = defaultdict(list)
            for _ in range(len(queue)):
                idx, m_dir = queue.popleft()

                if idx < 0 or idx >= len(dominoes) or dominoes[idx] != '.':
                    continue

                to_change[idx].append(m_dir)

            for idx, dirList in to_change.items():
                if 'L' in dirList and 'R' in dirList:
                    continue

                dominoes[idx] = dirList[0]

                if dirList[0] == 'R':
                    queue.append((idx + 1, 'R'))
                else:
                    queue.append((idx - 1, 'L'))

        return "".join(dominoes)





        