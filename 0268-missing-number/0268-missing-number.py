class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        cur_max = max(nums)
        co = set(nums)

        for i in range(cur_max + 1):
            if i not in co:
                return i

        return cur_max + 1 
