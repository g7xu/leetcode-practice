# stack

# pointer to seg the path

# at the end, clean path

# O(n)
# O(n)

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p = 0

        while p < len(path):
            p2 = p

            if path[p2] == '/':
                p2 += 1
            else:
                while p2 < len(path) and path[p2] != '/':
                    p2 += 1
                
                seg = path[p:p2]
                if seg == '..':
                    if stack:
                        stack.pop()
                elif seg != '.':
                    stack.append(seg)

            p = p2

        res = ''

        for ele in stack:
            res += '/' + ele

        if not res:
            return '/'
        
        return res



