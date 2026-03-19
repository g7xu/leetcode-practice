from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        pair = 0
        solo = 0
        for num in nums:
            freq[num] += 1
            solo += 1
            
            if freq[num] == 2:
                pair += 1
                solo -= 2
                freq[num] = 0

        return [pair, solo]
