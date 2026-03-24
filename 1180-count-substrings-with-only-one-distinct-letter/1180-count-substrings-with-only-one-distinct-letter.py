class Solution:
    def countLetters(self, s: str) -> int:
        
        @cache
        def con_sum(s_len):
            if s_len == 1:
                return 1

            return s_len + con_sum(s_len - 1)

        sl = f = 0
        res = 0
        while f < len(s) - 1:
        
            if s[f] != s[f + 1]:
                res += con_sum(f - sl + 1)
                f += 1
                sl = f
                continue

            f += 1

        res += con_sum(f - sl +1)

        return res
