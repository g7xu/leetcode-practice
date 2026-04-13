class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = nums[0]
        global_min = nums[0]
        cur_max = cur_min = t = 0

        for num in nums:
            t += num

            cur_max += num
            cur_min += num

            if cur_max < num:
                cur_max = num

            if cur_min > num:
                cur_min = num

            global_max = max(global_max, num, cur_max)
            global_min = min(global_min, num, cur_min)

        return max(global_max, t - global_min) if global_max > 0 else global_max
