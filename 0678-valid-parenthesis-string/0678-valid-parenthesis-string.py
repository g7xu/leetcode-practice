# recursive 
# back

# helper

# input
## stack
## pointer

# if *, three cursive

# otherwise, normal

# output, true or false

class Solution:
    def checkValidString(self, s: str) -> bool:

        @cache
        def helper(stack, p, s):
            stack = list(stack)

            if p == len(s):
                if stack:
                    return False
                return True

            if s[p] == '(':
                stack.append('(')
                if helper(tuple(stack), p + 1, s):
                    return True
                stack.pop()
            elif s[p] == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
                if helper(tuple(stack), p + 1, s):
                    return True
                stack.append('(')
            else:
                # empty
                if helper(tuple(stack), p + 1, s):
                    return True

                # use (
                stack.append('(')
                if helper(tuple(stack), p + 1, s):
                    return True
                stack.pop()
                
                # use )
                if stack and stack[-1] == '(':
                    stack.pop()
                    if helper(tuple(stack), p + 1, s):
                        return True
                    stack.append('(')

            return False


        return helper(tuple(), 0, s)
            
        