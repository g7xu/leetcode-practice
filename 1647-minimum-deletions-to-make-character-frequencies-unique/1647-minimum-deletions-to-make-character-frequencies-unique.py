# [3, 3, 2]
# [1, 1, 0, 0]
          
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        bucket = [0] * (max(freq.values()) + 1) 

        res = 0
        for k, v in freq.items():
            if bucket[v] == 0:
                bucket[v] = 1
                continue

            p = v
            while bucket[p] != 0:
                p -= 1

            if p != 0:
                bucket[p] = 1
            
            res += v - p

        return res
            