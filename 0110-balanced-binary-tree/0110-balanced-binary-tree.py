# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node): # => Bool, depth
            if not node:
                return True, 0

            l_balance, l_d = helper(node.left)
            r_balance, r_d = helper(node.right)

            if not l_balance or not r_balance:
                return False, None

            if abs(l_d - r_d) > 1:
                return False, None

            return True, max(l_d, r_d) + 1


        is_balance, _ = helper(root)

        return is_balance 