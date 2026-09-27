# DFS with backtracking
from collections import defaultdict, deque

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:

        connections = defaultdict(list)
        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        queue = deque([0])
        child = defaultdict(list)
        parent = defaultdict(list)
        visited = set([0])

        while queue:

            curr = queue.popleft()
            
            for c in connections[curr]:
                if c in visited:
                    continue

                child[curr].append(c)
                parent[c].append(curr)

                visited.add(c)
                queue.append(c)

        # print(connections)
        # print(child)
        # print(parent)


        opened = [1] * (max(parent) + 1)
        opened[0] = 0
        opened[bob] = 0

        # print(opened)
        # print(parent)
        # print(child)
        def dfs(alice_idx, bob_idx, opened, amount):
            if alice_idx not in child:
                return 0

            if bob_idx != 0:
                bob_next = parent[bob_idx][0]
            else:
                bob_next = 0

            candidates = []
            
            opened[bob_next] = 0
            for alice_next in child[alice_idx]:
                # find change in score
                if alice_next == bob_next:
                    c = amount[alice_next] / 2
                elif opened[alice_next]:
                    c = amount[alice_next]
                else:
                    c = 0

                opened[alice_next] = 0
                
                candidates.append(
                    dfs(alice_next, bob_next, opened, amount) + c
                )

                opened[alice_next] = 1

            
            opened[bob_next] = 1
            # print(candidates)
            return int(max(candidates))
                




        return amount[0] + dfs(0, bob, opened, amount)