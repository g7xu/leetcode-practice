# DFS
# at each point, can I eitehr
# continue my chunk or switch my chunk
# 

class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s3:
            return not s1 and not s2

        # chose s1
        if s1 and s1[0] == s3[0]:
            if self.isInterleave(s1[1:], s2, s3[1:]):
                return True

        if s2 and s2[0] == s3[0]:
            if self.isInterleave(s1, s2[1:], s3[1:]):
                return True

        return False