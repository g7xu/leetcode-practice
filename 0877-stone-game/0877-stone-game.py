# even piles
# total is odd

# DFS
# recursion with memo

# helper (piles, s, e)

# try both combination


# return the higehst score alice can acieve
# do the comparsion at the end



class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def helper(s, e, isAlice):
            if isAlice:
                if s == e:
                    return piles[s], 0

                sa, sb = helper(s+1, e, False)
                ea, eb = helper(s, e - 1, False)
                if sa + piles[s] > ea + piles[e]:
                    return sa + piles[s], sb
                else:
                    return ea + piles[e], eb

            else:
                if s == e:
                    return 0, piles[s]

                sa, sb = helper(s+1, e, True)
                ea, eb = helper(s, e - 1, True)
                if sb + piles[s] > eb + piles[e]:
                    return sa, sb + piles[s]
                else:
                    return ea, eb + piles[e]

        a_s, b_s = helper(0, len(piles) - 1, True)

        return a_s > b_s