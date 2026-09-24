from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        res = 0
        flag = False
        for a in freq.values():
            if a % 2 == 0:
                res += a
            elif not flag:
                res += a
                flag = True
            else:
                res += a - 1

        return res



        # res = 1

        # def find_odd_p_len(i, s):
        #     res = 1

        #     l = i - 1
        #     r = i + 1

        #     while l >= 0 and r < len(s):
        #         if s[l] != s[r]:
        #             break
                
        #         res += 2
        #         l -= 1
        #         r += 1

        #     return res

        # def find_even_p_len(i, s):
        #     res = 0
        #     l = i
        #     r = i + 1

        #     while l >= 0 and r < len(s):
        #         if s[l] != s[r]:
        #             break
                
        #         res += 2
        #         l -= 1
        #         r += 1

        #     return res




        # for i in range(len(s)):
        #     # check odd
        #     res = max(
        #         find_odd_p_len(i, s),
        #         find_even_p_len(i, s)
        #     )

        # return res
        