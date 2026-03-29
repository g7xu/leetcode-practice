class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        @cache
        def helper(ps, pt, s, t, k):
            if ps >= len(s) or pt >= len(t):
                
                # finished op
                if ps >= len(s) and pt >= len(t) and k == 0:
                    return True

                if k and abs(len(s[ps:]) - len(t[pt:])) == k:
                    return True

                return False

            res = []

            if s[ps] == t[pt]:
                res.append(helper(ps + 1, pt + 1, s, t, k))

            if k >= 1:
                # insert
                res.append(helper(ps, pt + 1, s, t, k - 1))

                # delete
                res.append(helper(ps + 1, pt, s, t, k - 1))

                # replace
                if s[ps] != t[pt]:
                    res.append(helper(ps + 1, pt + 1, s, t, k - 1))
            
            return any(res)

        return helper(0, 0, s, t, 1)