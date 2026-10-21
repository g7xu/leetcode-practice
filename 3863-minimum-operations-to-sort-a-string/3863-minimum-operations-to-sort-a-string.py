class Solution:
    def minOperations(self, s: str) -> int:
        truth = "".join(sorted(list(s)))
        if s == truth:
            return 0


        if len(s) <= 1:
            return 1
        elif len(s) == 2:
            return -1
        else:
            if s[0] == truth[0] or s[-1] == truth[-1]:
                return 1

            for i in range(1, len(s) - 1):
                if s[i] == truth[0] or s[i] == truth[-1]:
                    return 2
            return 3