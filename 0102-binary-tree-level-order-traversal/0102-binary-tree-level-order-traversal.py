# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# just BFS would solve the problem

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()

                if not cur:
                    continue

                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)

            if level:
                res.append(level)

        return res
            