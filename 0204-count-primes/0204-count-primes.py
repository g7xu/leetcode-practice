# if 10

# then we need to check
# 9, 8, 7, 6, 5, 4, 3, 2, 1

# can't do, have to check the answer

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        prime = [True] * n
        prime[0] = False
        prime[1] = False

        res = 0
        for i in range(2, n):
            if not prime[i]:
                continue
            
            res += 1
        
            c = i * i
            while c < n: 
                prime[c] = False
                c += i

        return res

