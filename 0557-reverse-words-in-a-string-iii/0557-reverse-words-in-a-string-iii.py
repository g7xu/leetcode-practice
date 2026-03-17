class Solution:
    def reverseWords(self, s: str) -> str:
        def c_reverse(a, b, s):
            return s[:a] + s[a:b+1][::-1] + s[b+1:]

        ss = f = 0
        s = s + ' '
        while f < len(s):
            
            if s[f] == ' ':
                s = c_reverse(ss, f - 1, s)
                f += 1
                ss = f
                continue

            f += 1

        return s[:-1]

        


