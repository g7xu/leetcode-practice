class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idx_dict = dict()
        res = -1
        for i in range(len(s)):
            char = s[i]

            if char not in idx_dict:
                idx_dict[char] = [i, i]
            else:
                idx_dict[char][1] = i

            low, high = idx_dict[char]
            tmp = high - low - 1

            if tmp >= 0:
                res = max(res, tmp)

        return res