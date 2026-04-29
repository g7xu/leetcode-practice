from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        mapping = defaultdict(list)
        for a, b in edges:
            mapping[a].append(b)

        def dfs(node):
            if node in path:
                return float('inf')
            
            if node in visited:
                return 0

            visited.add(node)
            path.add(node)
            colorIndx = ord(colors[node]) - ord('a')
            count[node][colorIndx] = 1

            for nei in mapping[node]:
                if dfs(nei) == float('inf'):
                    return float('inf')
                for c in range(26):
                    count[node][c] = max(
                        count[node][c],
                        (1 if c == colorIndx else 0) + count[nei][c]
                    )

            path.remove(node)
            return 0


        n, res = len(colors), 0
        count = [[0] * 26 for _ in range(n)]
        visited, path = set(), set()
        for i in range(n):
            if dfs(i) == float('inf'):
                return -1
            res = max(res, max(count[i]))

        return res
        

        
            