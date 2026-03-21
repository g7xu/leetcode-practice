class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        small_max = sorted(nums)

        s = 0
        m = len(small_max) - 1

        p = 0
        while p < len(nums):
            if p % 2 == 0:
                nums[p] = small_max[s]
                s += 1
            else:
                nums[p] = small_max[m]
                m -= 1
            
            p += 1

        
            


