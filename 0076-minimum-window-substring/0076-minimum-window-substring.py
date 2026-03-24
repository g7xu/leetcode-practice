# sliding window
# counter logic

# logic

# counter for ABC => missing count, if 0 or neg, fulfill

# sliding window
# take in f, update counter

# while loop checking if the s is valid

# expand f again

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = defaultdict(int)

        for char in t:
            missing[char] += 1

        sl = f = 0
        missingC = len(missing)
        res = None
        while f < len(s):
            if s[f] in missing:
                missing[s[f]] -= 1
                if missing[s[f]] == 0:
                    missingC -= 1

            while missingC == 0 and sl <= f:
                if not res or f - sl + 1 < len(res):
                    res = s[sl: f + 1]

                if s[sl] in missing:
                    missing[s[sl]] += 1
                    if missing[s[sl]] == 1:
                        missingC += 1
                
                sl += 1


            f += 1
                
        if not res:
            return ""

        return res



        