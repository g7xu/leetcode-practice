class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        @cache
        def helper(p, s):
            if p >= len(s):
                return True

            for i in range(p + 1, len(s) + 1):
                if s[p: i] in wordDict and helper(i, s):
                    return True

            return False

        return helper(0, s)
