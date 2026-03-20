# counter

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        
        target_freq = defaultdict(int)
        
        for char in s1:
            target_freq[char] += 1
        remain = len(target_freq)


        cur_freq = defaultdict(int)
        for i in range(0, len(s1)):
            cur_freq[s2[i]] += 1

            if s2[i] in target_freq and cur_freq[s2[i]] == target_freq[s2[i]]:
                remain -= 1

        if remain == 0:
            return True

        s = 0
        e = len(s1) - 1
        while e < len(s2) - 1:

            cur_freq[s2[s]] -= 1
            if s2[s] in target_freq and cur_freq[s2[s]] == target_freq[s2[s]] - 1:
                remain += 1
            s += 1

            cur_freq[s2[e + 1]] += 1
            if s2[e + 1] in target_freq and cur_freq[s2[e +1]] == target_freq[s2[e + 1]]:
                remain -= 1
            e += 1
            
            if remain == 0:
                return True

        return False 

            

            



        

