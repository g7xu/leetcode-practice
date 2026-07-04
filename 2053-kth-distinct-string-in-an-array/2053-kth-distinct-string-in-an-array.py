from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)

        for t in arr:
            if freq[t] == 1:
                if k == 1:
                    return t
                else:
                    k -= 1
        
        return ""