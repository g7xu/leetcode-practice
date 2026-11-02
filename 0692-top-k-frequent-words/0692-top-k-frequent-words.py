from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1


        arr = [(c, w) for w, c in freq.items()]
        arr.sort(key = lambda x: (-x[0], x[1]))
        res = [w for _, w in arr][:k]

        return res
        