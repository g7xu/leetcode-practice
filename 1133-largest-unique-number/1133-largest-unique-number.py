class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        freq = Counter(nums)

        for i in range(len(nums) - 1, -1, -1):
            if freq[nums[i]] == 1:
                return nums[i]

        return -1