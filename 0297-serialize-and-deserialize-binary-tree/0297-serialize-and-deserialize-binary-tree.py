# handling binary tree
# each node has 0 or 1 or 2 child



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ['']

        def r_serialize(node, res):
            if not node:
                res[0] += 'None,'
                return

            res[0] += str(node.val) + ','

            r_serialize(node.left, res)
            r_serialize(node.right, res)

        r_serialize(root, res)

        print(res)
        return res[0][:-1]

        

        
    from collections import deque        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        queue = deque(data.split(','))

        def r_deserialize(queue):
            if not queue:
                return
            
            if queue[0] == 'None':
                queue.popleft()
                return None
            
            val = int(queue.popleft())
            root = TreeNode(val)
            root.left = r_deserialize(queue)
            root.right = r_deserialize(queue)
            return root


        return r_deserialize(queue)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))