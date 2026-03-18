# increasing order --> pointer?

# fast and slow pointer
#

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = f = 0
        res = 0
        pre = None
        while f < len(nums):
            
            if pre is not None and nums[f] == pre:
                c += 1
            else:
                c = 1
                pre = nums[f]
            
            if c > 2:
                f += 1
                continue

            nums[s] = nums[f]
            s += 1
            f += 1
            res += 1

        return res
