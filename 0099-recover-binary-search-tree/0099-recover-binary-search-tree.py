# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) -> O(1)
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node1 = node2 = prev = None
        curr = root

        while curr:
            if curr.left is None:
                # comapre
                if prev and prev.val > curr.val:
                    node2 = curr
                    if node1 is None:
                        node1 = prev

                # move right
                prev = curr
                curr = curr.right

            else: # there is left subtree
                # find the pred
                pred = curr.left
                while pred.right is not None and pred.right != curr:
                    pred = pred.right

                
                if pred.right is None: # 牵线
                    pred.right = curr
                    curr = curr.left
                else: # 拆线
                    pred.right = None

                    # comapre
                    if prev and prev.val > curr.val:
                        node2 = curr
                        if node1 is None:
                            node1 = prev

                    # move right
                    prev = curr
                    curr = curr.right

        node1.val, node2.val = node2.val, node1.val
