# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs

# input, node

# check children and find the count and return True(uni) or False

# if both name is True and same value,
# return count + 1 and True

# return count and False 

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if not node:
                return 0, True

            lc, l_uni = helper(node.left)
            rc, r_uni = helper(node.right)

            if l_uni and r_uni:
                if node.left and node.left.val != node.val:
                    return lc + rc, False

                if node.right and node.right.val != node.val:
                    return lc + rc, False

                return lc + rc + 1, True
            else:
                return lc + rc, False

        
        res, _ = helper(root)
        return res
        

