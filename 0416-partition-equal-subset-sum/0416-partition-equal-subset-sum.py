# 1 1 11 11

# group1 = 11 1
# group2 = 11 1

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums) 

        if t % 2 == 1:
            return False
        else:
            t = t // 2

        p = set([0])

        for num in nums:
            for ele in list(p):
                if num + ele == t:
                    return True
                
                p.add(num + ele)

        return False 
        