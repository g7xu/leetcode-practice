from collections import defaultdict

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = defaultdict(int)

        for num in arr1:
            while num != 0:
                prefix[num] += 1
                num = num // 10



        res = 0
        for num in arr2:
            while num != 0 and len(str(num)) > res:
                if num in prefix:
                    res = len(str(num))
                    break
                
                num = num // 10

        return res


