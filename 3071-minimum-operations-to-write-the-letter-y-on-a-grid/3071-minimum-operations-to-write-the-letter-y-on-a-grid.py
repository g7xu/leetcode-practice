# find the Y shape

# Y: 0, 1, 2
# other: 0, 1, 2

# Y
# total
# 0, 1, 2 

# 3 types

# other
# total
# 0, 1, 2

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        half = n // 2

        y_feq = {0:0, 1:0, 2:0}
        o_feq = {0:0, 1:0, 2:0}

        for i in range(n):
            for j in range(n):
                if i <= half:
                    if i == j or i + j == n - 1:
                        y_feq[grid[i][j]] += 1
                    else:
                        o_feq[grid[i][j]] += 1
                else:
                    if j == half:
                        y_feq[grid[i][j]] += 1
                    else:
                        o_feq[grid[i][j]] += 1

        
        y_t = sum(y_feq.values())
        o_t = sum(o_feq.values())

        res = n * n
        for ynum, yc in y_feq.items():
            for onum, oc in o_feq.items():
                if onum == ynum:
                    continue

                tmp = y_t - yc + o_t - oc
                res = min(res, tmp)

        return res
