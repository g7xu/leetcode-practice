# binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        
        l = 0
        r = h * w - 1

        while True:
            if r - l <= 1:
                return matrix[l // w][l % w] == target or matrix[r // w][r % w] == target
            

            m = (l + r) // 2
            currrent = matrix[m // w][m % w]

            if currrent == target:
                return True
            elif currrent < target:
                l = m + 1
            else:
                r = m - 1


