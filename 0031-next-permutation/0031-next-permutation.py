# keep pushing the last element to the front until there is a smaller
# 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 1
        while idx > 0:
            if nums[idx] > nums[idx - 1]:
                break

            idx -= 1

        if idx == 0:
            nums.sort()
            return


        for i in range(len(nums) - 1, idx - 1, -1):
            if nums[i] > nums[idx - 1]:
                nums[i], nums[idx-1] = nums[idx-1], nums[i]

                s = idx
                e = len(nums) -1
                while s < e:
                    nums[s], nums[e] = nums[e], nums[s]
                    s += 1
                    e -= 1
                return









        