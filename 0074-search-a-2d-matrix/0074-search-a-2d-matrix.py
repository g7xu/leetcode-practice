# binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        
        l = 0
        r = h * w - 1

        while r - l > 1:
            

            m = (l + r) // 2
            
            col = m % w
            row = m // w
            

            # print(matrix[r][c])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1

            print(l, r)
        if matrix[l // w][l % w] == target or matrix[r // w][r % w] == target:
            return True

        return False

