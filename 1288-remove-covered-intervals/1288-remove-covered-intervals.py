class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda i : (i[0], -i[1]))
        res = 0
        max_e = None
        for s, e in intervals:
            if not max_e:
                res += 1
                max_e = e
                continue

            if e <= max_e:
                continue
            
            max_e = e
            res += 1

        return res
