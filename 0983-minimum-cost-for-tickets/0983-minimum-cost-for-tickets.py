# DFS

# return minimum cost

# p, days, costs

# if outside the range, return 0
# try all three different options, and return the minmum val

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @cache
        def helper(p):
            if p >= len(days):
                return 0

            
            res = []
            for day_pass, cost in zip([1, 7, 30], costs):
                end = days[p] + day_pass - 1
                np = p
                while np < len(days) and days[np] <= end:
                    np += 1

                res.append(cost + helper(np))

            return min(res)

        return helper(0)

            
