# challenge for this problem

# has negative number
# negative number at certain substring might be larger possitve with large negative

# the trick keep track of minimum and and maximum number

# [2,3,-2,4]

res = 6

# min = -12
# max = -2

1 



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        
        curMin = curMax = 1

        for num in nums:
            if num == 0:
                curMin = curMax = 1
                continue

            curMax, curMin = max(curMax * num, curMin * num, num), min(curMax * num, curMin * num, num)
            res = max(res, curMax)

        return res


        
         