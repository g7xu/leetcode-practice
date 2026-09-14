r""" Thinking area

accumulatiive sum

and pointier

O(n^2)

"""

from collections import defaultdict

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)

        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum += num

            if curr_sum % k == 0:
                res += 1

            res += freq[curr_sum % k]


            freq[curr_sum % k] += 1

        return res
