"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root])

        curlen = 0
        level = 1
        while queue:
            cur = queue.popleft()
            curlen += 1

            if cur is None:
                continue

            queue.append(cur.left)
            queue.append(cur.right)
            
            if curlen == level: 
                level *= 2
                curlen = 0
            else:    
                cur.next = queue[0]
                

        return root


            

