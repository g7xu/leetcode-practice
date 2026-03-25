# helper

# r, c, maxMove, m, n

# if maxMove == 0, return 1


# try four direction 

# if going out of boundary, return 1

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def helper(r, c, maxMove, m, n):
            if maxMove == 0:
                return 0

            t = 0
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    t += 1
                else:
                    t =  (t + helper(nr, nc, maxMove - 1, m, n)) % MOD

            return t

            

        return helper(startRow, startColumn, maxMove, m, n)