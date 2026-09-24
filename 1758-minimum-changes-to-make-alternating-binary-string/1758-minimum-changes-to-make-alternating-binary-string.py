class Solution:
    def minOperations(self, s: str) -> int:
        s0_c = s1_c = 0 
        a = 0

        for e in s:
            if int(e) == a:
                s1_c += 1
            else:
                s0_c += 1

            a = 1 if a == 0 else 0

        return min(s0_c, s1_c)
