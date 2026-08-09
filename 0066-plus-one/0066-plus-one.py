class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0] + digits

        res[-1] += 1
        for i in range(len(res) -1, -1, -1):
            if res[i] == 10:
                res[i] = 0
                res[i-1] += 1

        if res[0] == 0:
            return res[1:]

        return res

            
        