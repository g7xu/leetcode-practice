# 11, 4
# 7, 3 + 2 = 5
# 6, 2 + 2 + 2 = 6
# 3, 1 + 2 + 3 + 3 = bad

# binary search



# [3, 6, 7, 11]

# n log n
# left if: satified
# right if: not satified
# pick that number going right and check against the limit

# 

# binary search func (l, l_idx, r, r_idx)



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)

        def cal_cost(idx, k):
            res = idx
            while idx < len(piles):
                res += piles[idx] // k 
                res += 0 if piles[idx] % k == 0 else 1
                idx += 1
            return res

        @cache
        def find_cost(k):
            l = 0
            r = len(piles) - 1
            
            while l < r - 1:
                m = (l + r ) // 2

                if piles[m] == k:
                    return cal_cost(m, k)
                elif piles[m] >= k:
                    r = m 
                else:
                    l = m

            return cal_cost(l, k)

        lk = 1
        rk = piles[-1]
        while lk < rk - 1:
            mk = (lk + rk) // 2
            
            mk_cost = find_cost(mk)

            if mk_cost <= h:
                rk = mk
            else:
                lk = mk

        if find_cost(lk) <= h:
            return lk
        else:
            return rk

            