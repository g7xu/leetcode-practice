# DFS problem, we either choose or we skip

# helper
# input (p, target, cur)

# target == 0, save result

# target < 0, return

# make choice with for loop

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates, reverse=True)

        cur = []
        def helper(p, target):
            if target == 0:
                res.append(cur[::])
                return

            if target < 0:
                return

            while p < len(candidates) and candidates[p] > target:
                p += 1

            if p >= len(candidates):
                return


            # choose
            cur.append(candidates[p])
            helper(p, target - candidates[p])
            cur.pop()


            helper(p + 1, target)
            


        helper(0, target)
        return res

        