from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        t = Counter(p)
        matched = 0

        curr_word = defaultdict(int)
        for c in s[:len(p)]:
            curr_word[c] += 1

            if c not in t and curr_word[c] == 1:
                matched -= 1
            elif curr_word[c] == t[c]:
                matched += 1
            elif curr_word[c] == t[c] + 1:
                matched -= 1

        if matched == len(t):
            res = [0]
        else:
            res = []

        start = 0
        end = len(p) - 1
        while end < len(s) - 1:
            # remove
            curr_word[s[start]] -= 1
            if s[start] not in t and curr_word[s[start]] == 0:
                matched += 1
            
            if s[start] in t:
                if curr_word[s[start]] == t[s[start]]:
                    matched += 1
                elif curr_word[s[start]] == t[s[start]] - 1:
                    matched -= 1

            # adding
            curr_word[s[end + 1]] += 1
            if s[end + 1] not in t and curr_word[s[end + 1]] == 1:
                matched -= 1
            
            if s[end + 1] in t:
                if curr_word[s[end + 1]] == t[s[end + 1]]:
                    matched += 1
                elif curr_word[s[end + 1]] == t[s[end + 1]] + 1:
                    matched -= 1 

            # if start + 1 >= 19:
            #     # print(curr_word, matched)
            #     # print(t, len(t))
            #     # print("----")


            if matched == len(t):
                res.append(start + 1)

            start += 1
            end += 1

        return res
        


