r""" Thinking area

dfs with memo ctual just DFS


"""

# ideas
# 


# terminal
## find the word
## no where to go
## wrong char

# current
# check the word
# next one

# input
# word
# cur_ind
# visit

# output
# no

# backtracking


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])



        def search(visitd, word_idx, x, y):

            if board[x][y] != word[word_idx]:
                return False
            elif word_idx == len(word) - 1:
                return True

            visitd.add((x, y))
            res = False
            for x_d, y_d in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = x + x_d
                ny = y + y_d

                if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visitd:
                    res = search(visitd, word_idx + 1 , nx, ny)

                if res:
                    break

            visitd.remove((x, y))
            return res


        for i in range(n):
            for j in range(m):
                if search(set(), 0, i, j):
                    return True

        return False


            


        