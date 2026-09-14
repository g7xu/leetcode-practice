r""" Thinking area

n log n

sorted

two pointer

first dif, and then do linear to find the responding idx and replace


"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numList = [int(ele) for ele in list(str(num))]

        best = sorted(numList, key = lambda x: -x)

        p = 0
        tmp_best = None
        tmp = None
        while p < len(numList):
            if best[p] != numList[p]:
                tmp = numList[p]
                tmp_best = best[p]
                numList[p] = best[p]
                break
            
            p += 1

        if tmp_best is not None:
            for i in range(len(numList) - 1, -1, -1):
                if numList[i] == tmp_best:
                    numList[i] = tmp
                    break


        res = 0
        for i in range(len(numList)):
            res *= 10
            res += numList[i]
        
        return res



            