# binary search
# when equal go left

# when equal go right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        

        def bst_left(nums, target):
            l = 0
            r = len(nums) - 1

            while l < r - 1:
                m = (l + r) // 2

                if nums[m] >= target:
                    r = m
                else:
                    l = m

            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            return -1


        def bst_right(nums, target):
            l = 0
            r = len(nums) - 1

            while l < r - 1:
                m = (l + r) // 2

                if nums[m] <= target:
                    l = m
                else:
                    r = m

            if nums[r] == target:
                return r
            elif nums[l] == target:
                return l

            return -1

        return [
            bst_left(nums, target),
            bst_right(nums, target)
        ]
