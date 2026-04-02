# x == 0 or x == len(board) - 1 or y == 0 or y == len(board[x]) - 1

# check surrounding 

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        not_change = set()

        for i in range(len(board)):
            if i == 0 or i == len(board) - 1:
                temp = range(0, len(board[i]))
            else:
                temp = [0, len(board[i]) - 1]

            for j in temp:
                if (i, j) not in not_change and board[i][j] == 'O':
                    queue = deque([(i, j)])
                    not_change.add((i, j))

                    while queue:
                        x, y = queue.popleft()
                        

                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nx = x + dx
                            ny = y + dy

                            if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[nx]) and (nx, ny) not in not_change and board[nx][ny] == 'O':
                                queue.append((nx, ny))
                                not_change.add((nx, ny))

        
        print(not_change)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i, j) not in not_change:
                    board[i][j] = 'X'

                    
