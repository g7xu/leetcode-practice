class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def helper(p, S):
            if p >= len(S):
                return 1

            res = 0
            # fist digit
            if S[p] != '0':
                res += helper(p + 1, S)

            if p < len(S) - 1 and 10 <= int(S[p: p + 2]) <= 26:
                res += helper(p + 2, S)

            return res

        return helper(0, s)