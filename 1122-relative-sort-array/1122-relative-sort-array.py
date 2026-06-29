from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)

        res = []

        for ele in arr2:
            res += freq[ele] * [ele]
            del freq[ele]

        for k, v in sorted(freq.items()):
            res += v * [k]

        return res 

        