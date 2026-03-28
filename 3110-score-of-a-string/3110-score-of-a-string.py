class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre = ord(s[0])
        res = 0
        for i in range(1, len(s)):
            res += abs(pre - ord(s[i]))
            pre = ord(s[i])
            
        return res