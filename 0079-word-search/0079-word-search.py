
# input
## board
## visited
## word
## i
## cor

# ter
## word[i] != board[cor]
    ## return false

## if i == len(word) - 1
    ## return True


# cur
## mark curr cor visited
## check three directions
## check if in the bound and visited
## check func
## if getting true, return true 
## mark curr cor visited

# output
# return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def helper(board, visited, word, i, cor):
            r, c = cor
            
            if word[i] != board[r][c]:
                return False

            if i == len(word) - 1:
                return True

            visited[r][c] = 1
            for mr, mc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr = r + mr
                nc = c + mc

                if nr >= 0 and nr < len(visited) and nc >= 0 and nc < len(visited[nr]) and visited[nr][nc] == 0:
                    re = helper(board, visited, word, i + 1, (nr, nc))

                    if re:
                        return True 

            visited[r][c] = 0

            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                s_re = helper(board, [[0] * len(r) for r in board], word, 0, (r, c))

                if s_re:
                    return True


        return False