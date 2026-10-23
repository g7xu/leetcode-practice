# colBuckets
# rowBukcets

from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.colBuckets = defaultdict(set)
        self.rowBukcets = defaultdict(set)
        self.points = defaultdict(int)
        
    def add(self, point: list[int]) -> None:
        x, y = point
        self.colBuckets[x].add(y)
        self.rowBukcets[y].add(x)
        self.points[(x, y)] += 1
        

    def count(self, point: list[int]) -> int:
        res = 0
        x, y = point

        # print(self.colBuckets[x])
        # print(self.rowBukcets[y])
        # print(self.points)


        for v_can in self.colBuckets[x]:
            for h_can in self.rowBukcets[y]:
                if abs(v_can - y) != abs(h_can - x) or v_can == y or h_can == x:
                    continue

                if (h_can, v_can) in self.points:
                    res += self.points[(h_can, v_can)] * self.points[(x, v_can)] * self.points[(h_can, y)]

        return res
                


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)