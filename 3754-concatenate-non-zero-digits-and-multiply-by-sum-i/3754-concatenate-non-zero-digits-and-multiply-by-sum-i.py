class Solution:
    def sumAndMultiply(self, n: int) -> int:
        t = 0
        res = 0
        p = 1
        while n > 0:
            lst = n % 10

            if lst != 0:
                t += lst
                res += lst * p
                p *= 10

            n = n // 10

        return res * t

            
