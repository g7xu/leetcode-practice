r""" Thinking area

parent has coin, child don't have coin

child has coin, parent don't have coin


graph, point with more coins as epxanding. BFS

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [0]

        def helper(node):
            if node is None:
                return 0 

            left_val = helper(node.left)
            right_val = helper(node.right) 

            curr = left_val + right_val - 1 + node.val

            res[0] += abs(curr)

            return curr
    
        helper(root)
        return res[0]


        