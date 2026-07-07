# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        

        def helper(node):
            if node is None:
                return 0, 0, 0

            l_sum, l_c, l_m = helper(node.left)
            r_sum, r_c, r_m = helper(node.right)

            t = l_sum + node.val + r_sum
            c = l_c + r_c + 1

            return t, c, max(l_m, r_m, t / c)

        return helper(root)[-1]