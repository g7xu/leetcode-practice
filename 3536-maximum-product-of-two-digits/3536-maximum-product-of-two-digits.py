class Solution:
    def maxProduct(self, n: int) -> int:
        a = None
        b = None

        while n > 0:
            digit = n % 10
            n = n // 10
            print(digit)
            if a is None:
                a = digit
            elif digit >= a:
                b = a
                a = digit
            elif b is None:
                b = digit
            elif digit > b:
                b = digit

        print(a, b)
        return a * b