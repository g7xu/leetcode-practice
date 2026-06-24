class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = [0, 0]
        hashset = set()
        for row in grid:
            for entry in row:
                if entry in hashset:
                    res[0] = entry
                else:
                    hashset.add(entry)

        for i in range(1, len(grid) ** 2 + 1):
            if i not in hashset:
                res[1] = i
                break

        return res 
