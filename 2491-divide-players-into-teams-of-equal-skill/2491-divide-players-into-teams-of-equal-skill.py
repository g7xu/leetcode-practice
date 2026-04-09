# sorting?
# 1 2 3 3 4 5

# decision tree ?
# try all possibilities
# O(n^2)

# two sum 变种

# sort the array
# with a extra array tracking used
# 

# counter

# two sum with a target

from collections import defaultdict

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        freq = defaultdict(int)
        p_min, p_max = skill[0], skill[1]

        for v in skill:
            freq[v] += 1
            p_min = min(p_min, v)
            p_max = max(p_max, v)

        t = p_max + p_min

        res = 0
        for i in range(len(skill)):
            cur_val = skill[i]
            if freq[cur_val] == 0:
                continue


            freq[cur_val] -= 1

            dif = t - cur_val

            if freq[dif] <= 0:
                return -1
            else:
                freq[dif] -= 1
                # print(cur_val, dif)
                res += cur_val * dif

        return res


       