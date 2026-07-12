class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)


        @cache
        def dfs(r1, c1, r2, c2):

            res = grid[r1][c1]
            if r1 != r2 and c1 != c2:
                res += grid[r2][c2]

            if r1 == c1 == r2 == c2 == n - 1:
                return res

            can = []
            for dr1, dc1 in [[0, 1], [1, 0]]:
                nr1 = r1 + dr1
                nc1 = c1 + dc1

                if nr1 == n or nc1 == n or grid[nr1][nc1] == -1:
                    continue

                for dr2, dc2 in [[0, 1], [1, 0]]:
                    nr2 = r2 + dr2
                    nc2 = c2 + dc2

                    if nr2 == n or nc2 == n or grid[nr2][nc2] == -1:
                        continue

                
                    can.append(dfs(nr1, nc1, nr2, nc2))

            if not can or max(can) == -1:
                return -1
            

            return res + max(can)

        res = dfs(0, 0, 0, 0) 

        if res == -1:
            return 0

        return res 
