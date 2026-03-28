class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0: return True

        if len(t) == 0: return False
        
        ps = pt = 0

        while pt < len(t) and ps < len(s):
            
            if s[ps] == t[pt]:
                ps += 1

            pt += 1

        if ps != len(s):
            return False

        return True
        
        