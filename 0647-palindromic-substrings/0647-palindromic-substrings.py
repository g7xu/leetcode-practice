class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def helper(s, l, r):
            res = 0
            while True:
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    break
                
                res += 1
                l -= 1
                r += 1

            return res

        for i in range(len(s)):
            res += helper(s, i, i)

            if i < len(s) - 1:
                res += helper(s, i, i + 1)


            
        return res


