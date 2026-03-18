# increasing order --> pointer?

# fast and slow pointer
#

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = f = 1
        res = 1
        c = 1
        while f < len(nums):
            if nums[f] == nums[f - 1]:
                c += 1
                if c > 2:
                    f += 1
                    continue
            else:
                c = 1
            
            nums[s] = nums[f]
            s += 1
            f += 1
            res += 1

        return res
