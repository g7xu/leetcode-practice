class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        
        # @cache
        # def helper(left, right, x):
        #     if x == 0:
        #         return 0

        #     if x == -1 or right < left:
        #         return -1


        #     left_move = helper(left + 1, right, x - nums[left])
        #     right_move = helper(left, right - 1, x - nums[right])

        #     candidates = []

        #     if left_move != -1:
        #         candidates.append(left_move + 1)
                
        #     if right_move != -1:
        #         candidates.append(right_move + 1)

        #     if not candidates:
        #         return -1

        #     return min(candidates)

        # return helper(0, len(nums) - 1, x)


        # find the longest subtring equal to some number


        left = right = 0
        curr = 0
        target = sum(nums) - x
        res = None

        if target < 0:
            return -1

        while right < len(nums):
            curr += nums[right]

            while curr > target :
                # if left == right:
                #     left = right = right + 1
                #     curr = 0
                # else:
                curr -= nums[left]
                left += 1

            if curr == target:
                if not res:
                    res = len(nums) - right + left - 1
                else:
                    res = min(res, len(nums) - right + left - 1)

            right += 1


        if not res:
            return -1

        return res

                
