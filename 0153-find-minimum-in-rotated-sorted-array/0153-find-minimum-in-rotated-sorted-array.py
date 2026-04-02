# O(n)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        a = 0
        b = len(nums) - 1

        while b - a > 1:
            m = (a + b) // 2

            # left is sorted
            if nums[a] <= nums[m] <= nums[b]:
                b = m
            elif nums[a] <= nums[m]:
                a = m
            else:
                b = m

        return min(nums[a], nums[b])
        