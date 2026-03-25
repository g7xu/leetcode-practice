class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        unqiue_nums = sorted(list(set(nums)))

        if len(unqiue_nums) == 1:
            return sum(nums)


        earn1 = unqiue_nums[0] * count[unqiue_nums[0]]
        if unqiue_nums[0] + 1 == unqiue_nums[1]:
            earn2 = max(earn1, unqiue_nums[1] * count[unqiue_nums[1]])
        else:
            earn2 = earn1 + unqiue_nums[1] * count[unqiue_nums[1]]
        
        for i in range(2, len(unqiue_nums)):
            if unqiue_nums[i] - 1 == unqiue_nums[i - 1]:
                temp = max(unqiue_nums[i] * count[unqiue_nums[i]] + earn1, earn2)
            else:
                temp = unqiue_nums[i] * count[unqiue_nums[i]] + earn2


            earn1 = earn2
            earn2 = temp

        return earn2


