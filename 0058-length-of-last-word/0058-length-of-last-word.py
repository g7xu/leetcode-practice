class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = len(s) - 1

        while s[p] == ' ':
            p -= 1

        res = 0
        while p >= 0 and s[p] != ' ':
            res += 1
            p -= 1

        return res