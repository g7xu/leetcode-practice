r""" Thinking area



"""

from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq = Counter(s)

        for char in t:
            if char not in freq or freq[char] == 0:
                return char

            freq[char] -= 1

        # return 
