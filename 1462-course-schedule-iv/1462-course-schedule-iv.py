# we will use hashmap to keep track of all the course and their prerequest

# logic

# pre = dict(). course : {set of the request} # over we can use bucket to represent them

# step 1
# adj dict

# go over each node
# if not pre recod run dfs on this
# dfs (node, adj, pre)
# if node in pre, return
# go to the child
# union the resulting the child and their set
# return the resulting set


from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_dict = defaultdict(set)
        for a, b in prerequisites:
            adj_dict[b].add(a)


        def dfs(i, adj_dict, pre):
            if pre[i] != -1:
                return

            res = set()

            for ne in adj_dict[i]:
                dfs(ne, adj_dict, pre)

                res = res.union(pre[ne])
                res.add(ne)

            pre[i] = res

            

        pre = [-1] * numCourses
        for i in range(numCourses):
            dfs(i, adj_dict, pre)

        res = []
        for a, b in queries:
            res.append(pre[b] != -1 and a in pre[b])

        return res

        

