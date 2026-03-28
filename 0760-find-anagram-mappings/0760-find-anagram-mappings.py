from collections import defaultdict

class Solution(object):
    def anagramMappings(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mapping = defaultdict(list)

        for idx, num in enumerate(nums2):
            mapping[num].append(idx)

        res = []

        for num in nums1:
            res.append(mapping[num].pop())

        return res

        