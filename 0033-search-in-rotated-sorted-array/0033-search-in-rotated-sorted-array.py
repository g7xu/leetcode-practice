class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1

        while a <= b:
            m = (a + b) // 2

            print(a, b, m)

            if nums[m] == target:
                return m

            if nums[a] <= nums[m]:
                if nums[a] <= target < nums[m]:
                    b = m - 1
                else:
                    a = m + 1
            else:
                if nums[m] < target <= nums[b]:
                    a = m + 1
                else:
                    b = m - 1
        
        return -1
