"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = dict()

        new_head = Node(0)

        cur_o = head
        cur_n = new_head
        while cur_o:
            cur_n.next = Node(cur_o.val)
            mapping[cur_o] = cur_n.next
            cur_o = cur_o.next
            cur_n = cur_n.next

        cur_o = head
        cur_n = new_head.next
        while cur_o:
            if cur_o.random:
                cur_n.random = mapping[cur_o.random]

            cur_o = cur_o.next
            cur_n = cur_n.next

        return new_head.next



        