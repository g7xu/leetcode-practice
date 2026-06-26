class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        l = 1
        r = x

        while l < r - 1:
            m = (l + r) // 2

            if m * m == x:
                return m
            elif m * m < x:
                l = m
            else:
                r = m

        return l