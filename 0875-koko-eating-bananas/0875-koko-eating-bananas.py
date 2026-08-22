
# best k

# upper bound: min(piles)
# lower bound: max(piles)

# binary search to find solution

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Ture or false
        def check_hr(k, piles, h):
            total = 0
            for pile in piles:
                total += pile // k
                if pile % k != 0:
                    total += 1

                if total > h:
                    return False

            return True

        l = 1
        r = max(piles)

        print(l)

        while l < r:
            m = (l + r) // 2
            print(l, r, m)


            if check_hr(m, piles, h):
                r = m 
            else:
                l = m + 1

        return r