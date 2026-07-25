class Solution:
    def maxProduct(self, n: int) -> int:
        a = b = 0

        while n > 0:
            digit = n % 10
            n = n // 10
            if digit >= a:
                b = a
                a = digit
            elif digit > b:
                b = digit

        return a * b