class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curr = 0

        for char in s:
            if char not in ['(', ')']:
                continue

            if char == '(':
                curr += 1
                res = max(res, curr)
            else:
                curr -= 1

        return res
