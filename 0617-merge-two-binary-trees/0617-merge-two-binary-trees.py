# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None


        def combineTree(t1, t2):

            t1.val += t2.val

            if t2.left:
                if not t1.left:
                    t1.left = TreeNode(0)
                combineTree(t1.left, t2.left)

            if t2.right:
                if not t1.right:
                    t1.right = TreeNode(0)
                combineTree(t1.right, t2.right)



        res = TreeNode(0)
        if root1 is not None:
            combineTree(res, root1)
        
        if root2 is not None:
            combineTree(res, root2)

        return res
