# doing a single shift once at the end

# do a mod by length of remove the full cycle

# doing a substring of shift

# implementatoin

# calculate the shift
# > 0 left
# < 0 right

# mod by the length

# do substring

class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        shifts = 0

        for d, a in shift:
            if d == 0:
                shifts += a
            else:
                shifts -= a

        if shifts == 0:
            return s

        shifts = shifts % len(s)

        if shifts > 0:
            return s[shifts:] + s[:shifts] 
        else:
            return s[shifts:] + s[:shifts]

    