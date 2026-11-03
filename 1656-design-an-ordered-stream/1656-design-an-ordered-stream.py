class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.arr = [None] * n

    def insert(self, idKey: int, value: str) -> list[str]:
        res = []
        self.arr[idKey - 1] = value

        if self.ptr >= len(self.arr) or self.arr[self.ptr] is None:
            return res

        
        while self.ptr < len(self.arr) and self.arr[self.ptr] is not None:
            res.append(self.arr[self.ptr])
            self.ptr += 1

        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)