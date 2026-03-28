class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bad = {'2', '3', '4', '5', '7'}

        revert = list(str(n))[::-1]

        for i in range(len(revert)):
            if revert[i] in bad:
                return False
            
            if revert[i] == '6':
                revert[i] = '9'
            elif revert[i] == '9':
                revert[i] = '6'

        print(revert)
        if int("".join(revert)) == n:
            return False

        return True
        