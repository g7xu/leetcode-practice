# DFS

# return minimum cost

# p, days, costs

# if outside the range, return 0
# try all three different options, and return the minmum val

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @cache
        def helper(p, end):
            if p >= len(days):
                return 0

            if days[p] <= end:
                return helper(p+1, end)

            res = []
            for day_pass, cost in zip([1, 7, 30], costs):
                res.append(cost + helper(p + 1, days[p] + day_pass - 1))

            return min(res)

        return helper(0, 0)

            
