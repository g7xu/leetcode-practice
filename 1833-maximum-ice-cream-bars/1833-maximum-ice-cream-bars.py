class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        val = [0] * max(costs)

        for cost in costs:
            val[cost - 1] += 1

        res = 0
        for i in range(len(val)):
            amount = min(coins // (i + 1), val[i])
            res += amount 
            coins -= amount * (i + 1)

            if not coins or i + 1 > coins:
                return res

        return res

            
            

            