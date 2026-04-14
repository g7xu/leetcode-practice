class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = len(matrix[0])
        col = len(matrix)
        goal = col * row
        x = y = 0
        dir_idx = 0
        
        row -= 1
        col -= 1
        res = [matrix[x][y]]
        
        first_row = True
        while len(res) < goal:
            if dir_idx % 2 == 0:
                for _ in range(row):
                    x += move[dir_idx][0]
                    y += move[dir_idx][1]

                    res.append(matrix[x][y])

                if first_row:
                    first_row = False
                else:
                    row -= 1

            else:
                for _ in range(col):
                    x += move[dir_idx][0]
                    y += move[dir_idx][1]

                    res.append(matrix[x][y])

                col -= 1

            dir_idx = (dir_idx + 1) % 4
            

        return res
            

            