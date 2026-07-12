class LinkNode:
    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = LinkNode(0)
        self.right = LinkNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = LinkNode(val, self.right.pre, self.right)
        self.map[val] = node
        self.right.pre = node
        node.pre.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, pre = node.next, node.pre
            next.pre = pre
            pre.next = next
            self.map.pop(val)

    def popleft(self):
        res = self.left.next.val
        self.pop(res)
        return res

    def update(self, val):
        self.pop(val)
        self.pushRight(val)


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyMapping = dict() # key -> value
        self.lfu = 0
        self.CountMapping = collections.defaultdict(int)
        self.ListMapping = collections.defaultdict(LinkedList)

    def _counter(self, key):
        freq = self.CountMapping[key]
        self.ListMapping[freq].pop(key)
        self.ListMapping[freq + 1].pushRight(key)
        self.CountMapping[key] += 1

        if freq == self.lfu and self.ListMapping[freq].length() == 0:
            self.lfu += 1

    def get(self, key: int) -> int:
        if key in self.keyMapping:
            self._counter(key)
            return self.keyMapping[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key not in self.keyMapping and self.cap == len(self.keyMapping):
            print(self.lfu)
            tmp = self.ListMapping[self.lfu].popleft()


            print(tmp)
            self.CountMapping.pop(tmp)
            self.keyMapping.pop(tmp)

        self.keyMapping[key] = value
        self._counter(key)
        self.lfu = min(self.lfu, self.CountMapping[key])



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)