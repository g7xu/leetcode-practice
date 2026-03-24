# counter check the char

# sliding window idea

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        input_s = s

        s = f = 0
        duplicate = 0
        res = 0
        while f < len(input_s):
            
            counter[input_s[f]] += 1
            if counter[input_s[f]] == 2:
                duplicate += 1

            while duplicate:
                counter[input_s[s]] -= 1
                if counter[input_s[s]] == 1:
                    duplicate -= 1
                
                s += 1

            res = max(res, f - s + 1)
            f += 1

        return res
        