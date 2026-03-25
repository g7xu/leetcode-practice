

# brute force would take O(n)


# Binary search

# 
[4,5,6,7,0,1,2]

[6,7,0,1,2,4,5]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums) - 1

        while True:
            m = (a + b) // 2
            print(a, b, m)

            if nums[m] == target:
                return m
            elif a == b:
                break
            # left side sorted
            elif nums[a] <= nums[m]:
                if nums[a] <= target <= nums[m]:
                    b = m - 1
                else:
                    a = m + 1
            else:
                if nums[m] <= target <= nums[b]:
                    a = m + 1
                else:
                    b = m - 1

            print(a, b)

        return -1
            

