class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if node is None:
                return True

            if left >= node.val or node.val >= right:
                return False

            # if node.left and node.left.val > node.val:
            #     return False
            
            # if node.right and node.right.val < node.val:
            #     return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

            

        return valid(root, float('-inf'), float('inf'))


        