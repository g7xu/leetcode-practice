


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        @cache
        def helper(nums, n):
            if not nums:
                return '0' * n
            
            if n == 1 and len(nums) == 2:
                return None
            elif n == 1 and nums[0] == '0':
                return '1'
            elif n == 1:
                return '0'

            group1 = []
            group0 = []

            for num in nums:
                if num[0] == '1':
                    group1.append(num[1:])
                else:
                    group0.append(num[1:])

            res = helper(tuple(group1), n -1)

            if res:
                return '1' + res
                
            res = helper(tuple(group0), n - 1)

            if res:
                return '0' + res

            
        return helper(tuple(nums), len(nums[0]))


        # @cache
        # def helper(nums):
        #     setNum = set(nums)
        #     if "1" in setNum and "0" in setNum:
        #         return None
        #     elif "1" in setNum:
        #         return '0'
        #     elif "0" in setNum:
        #         return '1'

        #     group1 = []
        #     group0 = []

        #     for num in nums:
        #         if num[0] == '1':
        #             group1.append(num[1:])
        #         else:
        #             group0.append(num[1:])

        #     if group1:
        #         res = helper(tuple(group1))

        #         if res:
        #             return '1' + res
                
        #     if group0:
        #         res = helper(tuple(group0))

        #         if res:
        #             return '0' + res

            
        # return helper(tuple(nums))

            