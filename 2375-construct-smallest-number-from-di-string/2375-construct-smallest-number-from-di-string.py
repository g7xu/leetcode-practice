# IIIDIDDD
# 123456978

# DDD
# 4321

# O(n^2) # O(81) # O(1)

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []

        for i in range(1, len(pattern) + 2):
            res.append(i)

        # process from back
        for i in range(len(pattern) - 1, -1, -1):

            while i < len(res) - 1:
                p = pattern[i]

                if p == 'D' and res[i] > res[i + 1]:
                    break
                if p == 'I' and res[i] < res[i + 1]:
                    break

                res[i], res[i + 1] = res[i + 1], res[i]
                i += 1                


        return "".join([str(ele) for ele in res])
