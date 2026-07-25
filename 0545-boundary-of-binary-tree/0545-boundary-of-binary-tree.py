# ideas
# four parts
# triverse the graph 4 times
# left, right, top and bottom
# always check the left child, if no left, go right, stop at leave node
# always check the right child, if no go left, stop at leave node
# inOrder treversa for the entire tree, we only record the leave node
# O(n) for both


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]

        # left
        curr = root.left
        while curr:
            if curr.left is not None:
                res.append(curr.val)
                curr = curr.left
            elif curr.right is not None:
                res.append(curr.val)
                curr = curr.right
            else:
                curr = None

        # leave
        def inOrder(node):
            if node is None:
                return

            if node.left is None and node.right is None:
                res.append(node.val)
                return

            inOrder(node.left)
            inOrder(node.right)

        if root.left is not None or root.right is not None:
            inOrder(root)

        # right 
        curr = root.right
        temp = []
        while curr:
            if curr.right is not None:
                temp.append(curr.val)
                curr = curr.right
            elif curr.left is not None:
                temp.append(curr.val)
                curr = curr.left
            else:
                curr = None

        return res + temp[::-1]

