class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for idx, w in enumerate(words):
            for idx2, w2 in enumerate(words):
                if idx == idx2:
                    continue

                if w in w2:
                    res.append(w)
                    break

        return res 