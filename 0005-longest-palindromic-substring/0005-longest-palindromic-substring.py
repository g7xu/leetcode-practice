# 两种解法
## pointer (n^2)
## DP


# solution 1
# go over each point, expand outside

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL_index = resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL_index = l
                    resLen = r - l + 1
                
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resL_index = l
                    resLen = r - l + 1
                
                l -= 1
                r += 1

        return s[resL_index: resL_index + resLen]