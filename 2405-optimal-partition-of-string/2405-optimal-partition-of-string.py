# general idea

# can I just apply the greedy idea with sliding window
# can't think of any counter example, will approach the problem greedy

# having a sliding window
# expand if that ele does not exist in the set
# reduce if there is duplicate

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        char_set = set() 
        l = r = 0
        while r < len(s):
            
            if s[r] in char_set:
                res += 1
                char_set = set()
                l = r

            char_set.add(s[r])
            r += 1

        return res + 1

        

                