class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        end = intervals[0][-1]

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s < end:
                res += 1
                end = min(end, e)
            else:
                end = e
        return res
