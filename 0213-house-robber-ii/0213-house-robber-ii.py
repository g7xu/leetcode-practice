r""" Thinking area



"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                tmp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = tmp

            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
        