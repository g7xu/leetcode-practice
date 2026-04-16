class MovingAverage:

    def __init__(self, size: int):
        self.prefix_sum = []
        self.size = size

    def next(self, val: int) -> float:
        if self.prefix_sum:
            self.prefix_sum.append(self.prefix_sum[-1] + val)
        else:
            self.prefix_sum.append(val)

        if len(self.prefix_sum) <= self.size:
            return self.prefix_sum[-1] / len(self.prefix_sum)
        else:
            return (self.prefix_sum[-1] - self.prefix_sum[-self.size - 1]) / self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)