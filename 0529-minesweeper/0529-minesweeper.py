from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        

        def reveal(r, c, board):
            # assuming valid
            # just reveal that cord
            # -1: mine
            # 0: empty
            # 1 - 8: number
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return -1
            else:
                mines = 0
                for mr, mc in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
                    nr = r + mr
                    nc = c + mc

                    if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[nr]) and board[nr][nc] in ['M','X']:
                        mines += 1
                
                if mines == 0:
                    board[r][c] = 'B'
                else:
                    board[r][c] = str(mines)
                
                return mines

        # BFS
        queue = deque([click])
        visited = set(tuple(click))
        while queue:
            # print(queue)
            top_click_r, top_click_c = queue.popleft()
            cur_res = reveal(top_click_r, top_click_c, board)
            if cur_res == 0:
                for mr, mc in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
                    nr = mr + top_click_r
                    nc = mc + top_click_c

                    if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[nr]) and board[nr][nc] in ['M','E', 'B'] and (nr, nc) not in visited:
                        queue.append([nr, nc])
                        visited.add((nr, nc))

            # print(board)

        return board

