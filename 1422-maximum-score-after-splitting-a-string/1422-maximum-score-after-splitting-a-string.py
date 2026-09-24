class Solution:
    def maxScore(self, s: str) -> int:
            
        prefix_zero = [0]

        for char in s:
            prefix_zero.append(
                prefix_zero[-1] + (1 if char == '0' else 0)
            )

        prefix_zero = prefix_zero[1:-1]

        postfix_one = [0]

        for i in range(len(s) - 1, -1, -1):
            postfix_one.append(
                postfix_one[-1] + (1 if s[i] == '1' else 0)
            )

        postfix_one = postfix_one[::-1][1:-1]


        res = 0

        for a, b in zip(prefix_zero, postfix_one):
            res = max(
                res,
                a + b
            )

        return res