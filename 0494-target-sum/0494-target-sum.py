# brute force -- try all 2^n

# recursion with memo
# input: idx, target # starting with that idx and moving forward different ways to achieve the target
# base: just 1
# or: try both sign and sum up the total ways


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def helper(idx, target):
            if idx == len(nums) -1:
                if abs(nums[idx]) == abs(target):
                    if nums[idx] == 0:
                        return 2
                    return 1
                return 0


            res = 0

            res += helper(idx + 1, target - nums[idx])
            res += helper(idx + 1, target + nums[idx])
                
            return res

        return helper(0, target) 