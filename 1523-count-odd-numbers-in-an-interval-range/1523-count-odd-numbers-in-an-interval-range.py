r""" Thinking area



"""

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        nums = high - low + 1

        if nums % 2 == 0:
            return nums // 2
        elif low % 2 == 1:
            return nums // 2 + 1
        else:
            return nums // 2