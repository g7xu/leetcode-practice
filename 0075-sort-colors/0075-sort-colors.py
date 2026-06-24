# merge sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(nums, a, b):
            

            if a == b:
                return

            m = (a + b) // 2
            helper(nums, a, m)
            helper(nums, m + 1, b)

            first = a
            second = m + 1
            while first <= m and second <= b:
                if nums[first] > nums[second]:
                    nums[first], nums[second] = nums[second], nums[first]
                    tmp = second
                    while tmp < b and nums[tmp] > nums[tmp + 1]:
                        nums[tmp], nums[tmp + 1] = nums[tmp + 1], nums[tmp]
                        tmp += 1


                first += 1

            print(nums, a, b)
            return

        helper(nums, 0, len(nums) - 1)
        return nums

