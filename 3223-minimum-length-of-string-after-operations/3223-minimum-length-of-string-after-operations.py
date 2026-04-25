class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0
        freq = Counter(s)
        for v in freq.values():
            if v % 2 == 0:
                res += 2
            else:
                res += 1

        return res