class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            for char in list(str(num)):
                res.append(int(char))

        return res
