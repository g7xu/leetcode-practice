class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        pre = ord(s[0])

        for i in range(1, len(s)):
            res += abs(pre - ord(s[i]))
            pre = ord(s[i])

        return res
