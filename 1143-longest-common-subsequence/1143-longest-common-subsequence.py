# DFS, pointer problem


# p1, p2





# return length

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def helper(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            res = 0
            if text1[p1] == text2[p2]:
                res = max(res, 1 + helper(p1 + 1, p2 + 1))

            res = max(res, helper(p1, p2 + 1))
            res = max(res, helper(p1 + 1, p2))

            return res

        return helper(0, 0)
