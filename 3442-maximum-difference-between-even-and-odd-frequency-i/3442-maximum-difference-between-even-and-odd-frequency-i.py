from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = min_odd = max_even = min_even = None

        freq = Counter(s)

        for k, v in freq.items():
            if v % 2 == 0:
                # if max_even is None:
                #     max_even = v
                # else:
                #     max_even = max(max_even, v)
                
                if min_even is None:
                    min_even = v
                else:
                    min_even = min(min_even, v)
            else:
                if max_odd is None:
                    max_odd = v
                else:
                    max_odd = max(max_odd, v)
                
                # if min_odd is None:
                #     min_odd = v
                # else:
                #     min_odd = min(min_odd, v)


        return max_odd - min_even


