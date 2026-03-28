# logic, prefix max from right to left

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = [-1]

        for i in range(len(arr) - 1, 0, -1):
            res.append(max(res[-1], arr[i]))

        return res[::-1]
        
