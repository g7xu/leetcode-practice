class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0

        for word in words:
            word = set(word)
            if word.issubset(allowed):
                res += 1

        return res