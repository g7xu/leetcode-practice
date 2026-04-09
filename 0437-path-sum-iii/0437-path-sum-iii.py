# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# helper function
# node, target

# taking all possible sums 
# update the counter, and possible sums

# return possible, counter



class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0


        def helper(n, t):
            res = 0
            if n.val == targetSum:
                res += 1

            paths = [n.val]


            if not n.left and not n.right:
                print(paths)
                return paths, res


            if n.left:
                l_paths, l_res = helper(n.left, t)
                res += l_res
                for path in l_paths:
                    new_val = path + n.val
                    
                    if new_val == targetSum:
                        res += 1
                    paths.append(new_val)
                    
            if n.right:
                r_paths, r_res = helper(n.right, t)
                res += r_res
                for path in r_paths:
                    new_val = path + n.val

                    if new_val == targetSum:
                        res += 1
                    paths.append(new_val)

            return paths, res

        hi, res = helper(root, targetSum)

        return res
            
