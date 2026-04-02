# choose or not choose
# 


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def helper(p, nums, cur, res):
            res.add(tuple(cur[::]))

            if p >= len(nums):
                return

            # choose
            cur.append(nums[p])
            helper(p + 1, nums, cur, res)
            cur.pop()
            
            # not choose
            while p + 1 < len(nums) and nums[p + 1] == nums[p]:
                p += 1     
            
            helper(p + 1, nums, cur, res)

            

        nums = sorted(nums)
        helper(0, nums, [], res)

        return [list(x) for x in res]

