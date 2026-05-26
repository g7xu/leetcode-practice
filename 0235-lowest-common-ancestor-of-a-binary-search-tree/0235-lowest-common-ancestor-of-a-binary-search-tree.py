# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# if current is one of them return that number
# two child return that number, return itself
# if one child is number, return that number
# if both none, return None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node, p, q):
            if node is None:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            left_child = helper(node.left, p, q)
            right_child = helper(node.right, p, q)

            if left_child and right_child:
                return node
            elif left_child is None and right_child is None:
                return None
            elif left_child:
                return left_child
            else:
                return right_child

        return helper(root, p, q)
            