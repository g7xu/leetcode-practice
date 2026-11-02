class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums = sorted(nums)
        m = nums[len(nums) // 2]
        return sum([abs(m - num) for num in nums])

        # avg = mean(nums)

        # if avg != int(avg):
        #     return min(
        #         sum([abs(int(avg) - num) for num in nums]),
        #         sum([abs(int(avg) + 1 - num) for num in nums])
        #     )
        # else:
        #     return sum([abs(avg - num) for num in nums])