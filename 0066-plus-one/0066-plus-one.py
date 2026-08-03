class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0] + digits
        idx = len(res) - 1
        while True:
            res[idx] += 1
            if res[idx] != 10:
                break

            res[idx] = 0 
            idx -= 1

        if res[0] == 1:
            return res

        return res[1:]
        