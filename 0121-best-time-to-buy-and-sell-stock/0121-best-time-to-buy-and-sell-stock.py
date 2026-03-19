# accumulative max and min?


# [None, 7, 1, 1, 1, 1] # sell
# [6, 6, 6, 6, 4, None] # buy

# We just need to have a two pointer solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        
        while r < len(prices):
            
            if prices[r] < prices[l]:
                l = r
                r = l + 1
                continue

            res = max(prices[r] - prices[l], res)
            r += 1


        return res



