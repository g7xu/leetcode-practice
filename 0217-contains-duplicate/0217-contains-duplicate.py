from collections import defaultdict

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = defaultdict(int)

        for num in nums:
            c[num] += 1
            if c[num] >= 2:
                return True

        return False