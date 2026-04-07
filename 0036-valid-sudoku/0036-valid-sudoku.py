class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_bucket = [set() for _ in range(9)]
        col_bucket = [set() for _ in range(9)]
        box_bucket = [[set() for _ in range(3)] for _ in range(3)] 

        for i in range(len(board)):
            for j in range(len(board[i])):
                str_num = board[i][j]
                
                if str_num == '.':
                    continue
                
                num = int(str_num)
                print(num)

                if num in row_bucket[i]:
                    return False
                row_bucket[i].add(num)

                if num in col_bucket[j]:
                    return False
                col_bucket[j].add(num)

                if num in box_bucket[i // 3][j // 3]:
                    return False
                box_bucket[i // 3][j // 3].add(num)


        return True
