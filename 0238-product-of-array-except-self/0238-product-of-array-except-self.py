class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front_trace = [] 
        back_trace = []

        # loop through the list from the front
        for i in range(len(nums)):
            if i == 0: front_trace.append(1)
            else:
                front_trace.append(front_trace[-1] * nums[i-1])

        # loop through the list from the back
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1: back_trace.append(1)
            else:
                back_trace.append(back_trace[-1] * nums[i + 1])
        back_trace = back_trace[::-1]

        # multiple them together since they completement each other

        return [front_trace[i] * back_trace[i] for i in range(len(back_trace))]
        
            