# O(n)

# use hasmap

class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """

        key_idx = dict()

        for idx, key in enumerate(keyboard):
            key_idx[key] = idx

        def find_dist(a, b, key_idx):
            return abs(key_idx[a] - key_idx[b])

        pre = keyboard[0]
        res = 0
        for key in word:
            res += find_dist(pre, key, key_idx)
            pre = key


        return res
        


        
        