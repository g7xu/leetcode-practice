class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        @cache
        def helper(val):
            res = 0
            for char in str(val):
                res += int(char)

            return res

        for i in range(len(nums)):
            if helper(nums[i]) == i:
                return i

        return -1
