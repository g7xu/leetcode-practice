# 两种解法
## pointer (n^2)
## DP


# solution 1
# go over each point, expand outside
# two pointer 去 expand, and keep track of the longest length

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         resL_index = resLen = 0

#         for i in range(len(s)):
#             l, r = i, i
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > resLen:
#                     resL_index = l
#                     resLen = r - l + 1
                
#                 l -= 1
#                 r += 1

#             l, r = i, i + 1
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > resLen:
#                     resL_index = l
#                     resLen = r - l + 1
                
#                 l -= 1
#                 r += 1

#         return s[resL_index: resL_index + resLen]


# solution 2 
# Top Down DP

# given two index, i, j

# if i == j - 1 and s[i] == s[j], return 1
# if i == j, return 1

# if s[i] == s[j], then dp[i][j] = recrusive(i + 1, j - 1)

# else false

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))] 

        def solve(i, j, s, dp):
            if dp[i][j] != -1:
                return dp[i][j]

            if i == j:
                dp[i][j] = 1
                return 1
            
            if s[i] == s[j]:

                if i + 1 == j:
                    dp[i][j] = 1
                    return 1

                dp[i][j] = solve(i + 1, j - 1, s, dp)
                return dp[i][j] 

            dp[i][j] = False
            return False

        
        res = ''
        resLen = 0
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if j < i:
                    continue

                if (solve(i, j, s, dp)) and j - i + 1 > resLen:
                    res = s[i : j + 1]
                    resLen = j - i + 1

        return res


                
