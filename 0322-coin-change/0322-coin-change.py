
# [....]


# compare to the previous one
# 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)[::-1]

        @cache
        def helper(i, amount):
            if amount == 0:
                return 0

            if i >= len(coins):
                return -1

            if coins[i] > amount:
                return helper(i + 1, amount)

            res = []

            non_skip = helper(i, amount - coins[i])
            if non_skip != -1:
                res.append(non_skip + 1)
            
            skip = helper(i + 1, amount)
            if skip != -1:
                res.append(skip)

            if res:
                return min(res)
            
            return -1


        return helper(0, amount)


