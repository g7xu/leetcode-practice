r""" Thinking area

DFS

node

param
- node

- go left == 
- go right ===

- get result


- return
- left sum, left count, right sum, right count, acc_sum


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(node):
            if node is None:
                return 0, 0, 0

            l_sum, l_c, l_res = helper(node.left)
            r_sum, r_c, r_res = helper(node.right)

            res = l_res + r_res
            if (l_sum + r_sum + node.val) // (l_c + r_c + 1) == node.val:
                res += 1

            return l_sum + r_sum + node.val, l_c + r_c + 1, res 

        _, _, res = helper(root)

        return res
        