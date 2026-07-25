# DFS
# i don't care about how many people

# recurssion

# input: node

# if leaf node:
# return 0

# cur(node)
# if there is cost, +2 and the cost

# output: cost

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        childs = collections.defaultdict(list)

        for a, b in edges:
            childs[a].append(b)
            childs[b].append(a)



        def helper(node, pre):
            c = 0

            if node not in childs:
                return c


            for child in childs[node]:
                if child == pre:
                    continue

                child_c = helper(child, node)
                if hasApple[child] or child_c:
                    c += 2

                c += child_c

            return c 

        return helper(0, None)

