# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, max_val): # good node count
            if not node:
                return 0

            res = 0
            if node.val >= max_val:
                res += 1

            max_val = max(max_val, node.val)
            res += helper(node.left, max_val)
            res += helper(node.right, max_val)

            return res

        if not root:
            return 0

        return helper(root, root.val)

        