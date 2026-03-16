# sliding window problem with counter

from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        limit = 2
        
        res = 0
        s = f = 0
        while f < len(fruits):
            freq[fruits[f]] += 1

            if freq[fruits[f]] == 1:
                limit -= 1

            while limit < 0:
                freq[fruits[s]] -= 1
                if freq[fruits[s]] == 0:
                    limit += 1

                s += 1

            res = max(res, f - s + 1)
            f += 1
            

        return res

        