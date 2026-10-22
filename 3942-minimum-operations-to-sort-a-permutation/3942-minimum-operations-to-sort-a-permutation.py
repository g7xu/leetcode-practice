class Solution:
    def minOperations(self, nums: List[int]) -> int:
        j = nums.index(0)
        n = len(nums)
        if all([nums[(k + 1) % n] == (nums[k] + 1) % n for k in range(n)]):
            return min(j, 2 + n - j)
        elif all([nums[(k + 1) % n] == (nums[k] - 1) % n for k in range(n)]):
            return min((j + 1) % n + 1, n - j)
        else:
            return -1

        # checking if there is a single cycle
        
