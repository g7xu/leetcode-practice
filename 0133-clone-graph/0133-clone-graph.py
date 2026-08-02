"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# can triverse the graph with BFS
# when create new node, create mapping from the old to new
# when making connections, check the mapping or create new node

# doing BFS
# for each disocvered node,
# check if we have a mapping already, if not create
# draw the connection
# the problem is solved when the BFS is complete
# O(n)
# O(n)

# using queue



from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        res = Node(node.val)
        queue = deque([node])
        mapping = {
            node : res
        }

        visited = set()
        while queue:
            curr_node = queue.popleft()
            visited.add(curr_node)

            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    continue

                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val)

                mapping[curr_node].neighbors.append(mapping[neighbor])
                mapping[neighbor].neighbors.append(mapping[curr_node])
                queue.append(neighbor)

        return res
        
        
        

        