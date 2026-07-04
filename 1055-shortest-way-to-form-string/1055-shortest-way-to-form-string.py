class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        p1 = p2 = 0
        res = 1
        while p2 < len(target):
            if p1 >= len(source):
                p1 = 0
                res += 1

            tmp = p1
            while source[p1] != target[p2]:
                p1 += 1
                if p1 >= len(source):
                    res += 1
                    p1 = 0

                if tmp == p1:
                    return -1

            p1 += 1
            p2 += 1

        return res 
            