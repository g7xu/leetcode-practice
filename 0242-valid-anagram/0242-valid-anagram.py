# two possible solution

# use counter
# speed: O(n)
# memory: O(n)

# use sorting in place
# speed: O(n log n)
# memory: O(1)

# 

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
        

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = defaultdict(int)
        for char in s:
           s_counter[char] += 1

        missing = len(s_counter)

        for char in t:
            s_counter[char] -= 1

            if s_counter[char] < 0:
                return False

            if s_counter[char] == 0:
                missing -= 1

        return missing == 0

         
        