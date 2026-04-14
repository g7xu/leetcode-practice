from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)

        for char in text:
            if char in 'balloon':
                freq[char] += 1

        res = 0

        while True:
            for k, v in dict({'b':1, 'a':1, 'l':2, 'o':2, 'n':1}).items():
                freq[k] -= v
                if freq[k] < 0:
                    return res

            res += 1
                    
