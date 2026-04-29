# set
# order doesn't matter
# 

# sliding winidow
# counter

# each step move with 1 unit and check if there is any dupliciate
# use a counter to check duplicate

from collections import defaultdict

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        res = 0
        freq = defaultdict(int)
        du = 0

        l = r = 0

        # init
        for _ in range(k):
            freq[s[r]] += 1
            if freq[s[r]] == 2:
                du += 1
            r += 1

        if du == 0:
            res += 1

        # moving
        while r < len(s):
            freq[s[r]] += 1
            if freq[s[r]] == 2:
                du += 1

            freq[s[l]] -= 1
            if freq[s[l]] == 1:
                du -= 1

            if du == 0:
                res += 1

            r += 1
            l += 1

        return res
        