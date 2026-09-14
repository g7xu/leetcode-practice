r""" Thinking area

sliding window 

dictionary to track the freq
value to track the distinct character


"""


from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        freq = defaultdict(int)
        distincts = 0
        res = 0

        slow = fast = 0
        while fast < len(s):

            freq[s[fast]] += 1
            if freq[s[fast]] == 1:
                distincts += 1

            while distincts > k:
                freq[s[slow]] -= 1
                if freq[s[slow]] == 0:
                    distincts -= 1

                slow += 1

            res = max(res, fast - slow + 1)
            fast += 1

        return res