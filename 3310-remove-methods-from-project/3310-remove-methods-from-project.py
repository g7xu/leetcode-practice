

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        indegree = collections.defaultdict(int)
        neighbors = collections.defaultdict(set)

        for a, b in invocations:
            neighbors[a].add(b)
            indegree[b] += 1

        # BFS
        queue = collections.deque([k])
        sus = set([k])
        while queue:
            curr = queue.popleft()

            for neighbor in neighbors[curr]:
                indegree[neighbor] -= 1
                if neighbor not in sus:
                    sus.add(neighbor)
                    queue.append(neighbor)


        for node in sus:
            if indegree[node] > 0:
                return list(range(n))

        return [i for i in range(n) if i not in sus]
                    

