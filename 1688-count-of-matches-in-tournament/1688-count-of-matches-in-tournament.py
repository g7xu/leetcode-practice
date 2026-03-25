# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         if n <= 1:
#             return 0

#         remain =  n // 2

#         if n % 2 == 0:
#             return remain + self.numberOfMatches(remain)
#         else:
#             return remain + self.numberOfMatches(remain + 1)

        
# there is actually a mathmatical trick
# every match eliminate one team, so get to only one team, we need to get rid of n - 1 team


class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1