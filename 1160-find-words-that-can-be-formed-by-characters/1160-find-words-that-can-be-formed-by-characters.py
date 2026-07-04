from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        have = Counter(chars)
        res = 0
        for word in words:
            freq = Counter(word)
            v = True
            for k, v in freq.items():
                if k not in have or have[k] < v:
                    v = False
                    break

            if v:
                res += len(word)

        return res
