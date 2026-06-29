class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = []
        w2 = []

        for idx, word in enumerate(wordsDict):
            if word == word1:
                w1.append(idx)
            
            if word == word2:
                w2.append(idx)

        res = len(wordsDict) - 1

        for idx_1 in w1:
            for idx_2 in w2:
                res = min(res, abs(idx_1 - idx_2))

        return res