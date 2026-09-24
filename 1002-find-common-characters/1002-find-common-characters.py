from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        shared = Counter(words[0])

        for i in range(1, len(words)):
            word = words[i]

            word_freq = Counter(word)

            for k in list(shared.keys()):
                if k not in word_freq:
                    del shared[k]
                else:
                    shared[k] = min(shared[k], word_freq[k])

        res = []

        for k, v in shared.items():
            for _ in range(v):
                res.append(k)

        return res