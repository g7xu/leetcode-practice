class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        change = []

        for a, b in intervals:
            change.append((a, 1))
            change.append((b, -1))

        change.sort()

        res = 0
        cur = 0
        for _, c in change:
            cur += c
            res = max(res, cur)

        return res 