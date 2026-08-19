# doubly linked LIst

class node:
    def __init__(self, url, prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.homePage = node(homepage)
        self.curr = self.homePage

    def visit(self, url: str) -> None:
        self.curr.next = node(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev is None:
                return self.curr.url

            self.curr = self.curr.prev

        return self.curr.url
        
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next is None:
                return self.curr.url

            self.curr = self.curr.next

        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)