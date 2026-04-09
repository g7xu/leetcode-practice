class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = None
        duplicate = None

        nums = sorted(nums)

        if nums[0] != 1:
            missing = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate = nums[i]
            elif nums[i] != nums[i - 1] + 1:
                missing = nums[i] - 1
            
        if missing is None:
            missing = nums[-1] + 1

        return [duplicate, missing]