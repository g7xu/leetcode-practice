# this is just a stack right 

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []

        for char in s:
            if char.isdigit():
                res.pop()
            else:
                res.append(char)

        return "".join(res)