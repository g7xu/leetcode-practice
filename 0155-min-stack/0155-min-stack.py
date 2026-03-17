class MinStack:

    def __init__(self):
        self.min_val = None
        self.minstack = []
        self.curmin = []

    
    def push(self, val: int) -> None:

        if not self.minstack or val < self.curmin[-1]:
            self.curmin.append(val)
        else:
            self.curmin.append(self.curmin[-1])

        self.minstack.append(val)


    def pop(self) -> None:
        self.curmin.pop(-1)
        return self.minstack.pop(-1)
        

    def top(self) -> int:
        return self.minstack[-1]
        

    def getMin(self) -> int:
        return self.curmin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()