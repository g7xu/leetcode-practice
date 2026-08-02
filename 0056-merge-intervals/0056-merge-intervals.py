class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        
        c_s, c_e = intervals[0]
        for s, e in intervals[1:]:
            if s > c_e:
                res.append([c_s, c_e])
                c_s = s
                c_e = e
                continue

            c_e = max(c_e, e)

        return res + [[c_s, c_e]]
