class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        mapping = dict()
        mapping2 = dict()

        for a, b in zip(s, t):
            if a in mapping and mapping[a] != b:
                return False

            if b in mapping2 and mapping2[b] != a:
                return False

            mapping[a] = b
            mapping2[b] = a

        return True