# two possible solution

# use counter
# speed: O(n)
# memory: O(n)

# use sorting in place
# speed: O(n log n)
# memory: O(1)

# 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        