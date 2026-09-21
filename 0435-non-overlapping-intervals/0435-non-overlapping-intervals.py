r""" Thinking area



"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda a: a[-1])

        res = 0
        lastest = float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0] < lastest:
                res += 1
                continue

            lastest = intervals[i][1]

        return res