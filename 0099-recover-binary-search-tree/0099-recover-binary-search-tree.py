# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # in order traversal -> sorted array
        l = []

        def inOrder(node):
            if node is None:
                return

            inOrder(node.left)
            l.append(node)
            inOrder(node.right)

        inOrder(root)

        # go through the array -> find invarsions
        i = 0 
        node1 = node2 = None
        while i < len(l) - 1:
            if l[i].val > l[i+1].val:
                if node1 is None:
                    node1 = l[i]
                    node2 = l[i+1]
                else:
                    node2 = l[i+1]
                    break

            i += 1

        # swap
        node1.val, node2.val = node2.val, node1.val
        return root