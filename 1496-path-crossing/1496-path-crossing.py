# 

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set([(0, 0)])
        x = y = 0

        for ele in path:
            if ele == 'N':
                y += 1
            elif ele == 'E':
                x += 1
            elif ele == 'S':
                y -= 1
            else:
                x -= 1


            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))

        return False
            
