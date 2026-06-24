# DFS with backtracking

# input
# nums, pointer, pendingList

# termination
# pointer outside of the nums -> adding the pendingList as an answer

# current recur
# update the answer list
# do for loop
# add the num at the pointer to the pendingList
# update the actual list
# call the func with pointer +1 
# remove that number


# output
# []
# [1]
# [1, 2]
# [1, 2, 3]
# [2]
# [2, 3]
# [3]

# [2 ]

# []
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 3]
# [2, 3]
# [3]



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        re = []

        def helper(nums, p, cl):
            re.append(cl[:])
            if p >= len(nums):
                return

            for i in range(p, len(nums)):
                cl.append(nums[i])
                helper(nums, i+1, cl)
                cl.pop()


        helper(nums, 0, [])

        return re