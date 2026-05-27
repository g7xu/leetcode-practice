from collections import defaultdict

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        idx_set = [defaultdict(int) for i in range(len(words[0]))]

        for word in words:
            for i in range(len(word)):
                idx_set[i][word[i]] += 1

        @cache
        def helper(i, k):
            if i >= len(target):
                return 1

            if k >= len(idx_set):
                return 0

            if target[i] not in idx_set[k]:
                return helper(i, k + 1)

            return helper(i + 1, k + 1) * idx_set[k][target[i]] + helper(i, k + 1)

        return helper(0, 0) % (10**9 + 7)