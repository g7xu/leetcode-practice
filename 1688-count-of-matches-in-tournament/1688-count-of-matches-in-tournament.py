class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n <= 1:
            return 0

        remain =  n // 2

        if n % 2 == 0:
            return remain + self.numberOfMatches(remain)
        else:
            return remain + self.numberOfMatches(remain + 1)

        

