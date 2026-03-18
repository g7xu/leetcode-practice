# brute force
## for loop n times

# using while loop here can achieve a space complexity of O(1) since no stack

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
            
        if n % 2 == 0:
            return self.myPow(x*x, n // 2)
        
        return x * self.myPow(x*x, n // 2)
        