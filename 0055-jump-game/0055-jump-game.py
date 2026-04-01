# [2, 4, 3, 4, 8]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        reach = []

        for idx, num in enumerate(nums):
            reach.append(idx + num)

        t = len(reach) - 1
        limit = None

        print(reach)
        for i in range(len(reach)):
            print(i, "...", limit)

            if limit is None:
                limit = reach[i]

            if i > limit:
                return False

            if reach[i] >= t:
                return True

            limit = max(limit, reach[i])
            print(limit)
            print(t)

        return False


        
        