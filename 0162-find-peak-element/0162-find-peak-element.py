class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            middle = (left + right) // 2

            if middle == 0:
                break
            elif nums[middle - 1] < nums[middle] > nums[middle + 1]:
                return middle
            elif nums[middle - 1] < nums[middle] < nums[middle + 1]:
                left = middle 
            else:
                right = middle

        if nums[left] > nums[right]:
            return left

            
        return right