class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        bucket = defaultdict(int)

        l = r = 0
        res = 0
        while r < len(s):
            # update my bucket
            bucket[s[r]] += 1

            # reduce
            while bucket[s[r]] >= 2:
                bucket[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res