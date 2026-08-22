class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1

        temp = n
        while temp != 0:
            digit = temp % 10
            temp = temp // 10

            digit_sum += digit
            digit_product *= digit

        return n % (digit_product + digit_sum) == 0