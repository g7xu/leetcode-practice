class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = Counter(s)

        used = False
        for f in freq.values():
            if f % 2 != 0:
                if used:
                    return False
                else:
                    used = True
        
        return True

        
            