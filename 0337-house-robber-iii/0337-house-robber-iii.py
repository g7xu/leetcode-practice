# DFS
# 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        

        def helper(node):
            if node is None:
                return (0, 0)

            left_curr, left_skip = helper(node.left)
            right_curr, right_skip = helper(node.right)

            include_curr = node.val + left_skip + right_skip
            not_include_curr = left_curr + right_curr

            return (max(include_curr, not_include_curr), not_include_curr)




        return max(helper(root))