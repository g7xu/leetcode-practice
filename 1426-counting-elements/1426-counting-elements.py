class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        exist = set(arr)

        res = 0
        for num in arr:
            if num + 1 in exist:
                res += 1

        return res 