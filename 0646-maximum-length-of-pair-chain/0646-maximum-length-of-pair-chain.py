# no pair, get 0
# single pair, get 1

# DP - bottom up

# [[2, 1], [1, 2], [1, 3]]

# O(n^2)

# [[], [], [1, 3]]

# class Solution:
    # def findLongestChain(self, pairs: List[List[int]]) -> int:
        # pairs = sorted(pairs)
        
        # dp = [None] * len(pairs)

        # dp[-1] = [1, pairs[-1][0]]

        # for i in range(len(pairs) - 2, -1, -1):
            
        #     cur_idx = i + 1
        #     best = None
        #     while cur_idx < len(dp):
        #         if pairs[i][1] < dp[cur_idx][1]:
        #             if not best:
        #                 best = dp[cur_idx][0]
        #             else:
        #                 best = max(best, dp[cur_idx][0])
                
        #         cur_idx += 1

        #     dp[i] = [1, pairs[i][0]]

        #     if best:
        #         dp[i][0] += best

        # # print(pairs)
        # # print(dp)

        # return max([i for i, _ in dp])



class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda pair: pair[-1])

        res = 1
        end = pairs[0][1]

        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                res += 1
                end = pairs[i][1]
            
        return res
        
      