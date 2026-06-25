# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# hashmap

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        child = set()


        for p, c, left in descriptions:            
            if p not in nodes:
                nodes[p] = TreeNode(p)

            if c not in nodes:
                nodes[c] = TreeNode(c)
            
            p = nodes[p]
            c = nodes[c]
            child.add(c)


            if left:
                p.left = c
            else:
                p.right = c

        for node in nodes.values():
            if node not in child:
                return node