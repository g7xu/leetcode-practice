# recursive 
# back

# helper

# input
## stack
## pointer

# if *, three cursive

# otherwise, normal

# output, true or false


# this is the stupid way of solving this problem mannnn
# class Solution:
#     def checkValidString(self, s: str) -> bool:

#         @cache
#         def helper(stack, p, s):
#             stack = list(stack)

#             if p == len(s):
#                 if stack:
#                     return False
#                 return True

#             if s[p] == '(':
#                 stack.append('(')
#                 if helper(tuple(stack), p + 1, s):
#                     return True
#                 stack.pop()
#             elif s[p] == ')':
#                 if not stack or stack[-1] != '(':
#                     return False
#                 stack.pop()
#                 if helper(tuple(stack), p + 1, s):
#                     return True
#                 stack.append('(')
#             else:
#                 # empty
#                 if helper(tuple(stack), p + 1, s):
#                     return True

#                 # use (
#                 stack.append('(')
#                 if helper(tuple(stack), p + 1, s):
#                     return True
#                 stack.pop()
                
#                 # use )
#                 if stack and stack[-1] == '(':
#                     stack.pop()
#                     if helper(tuple(stack), p + 1, s):
#                         return True
#                     stack.append('(')

#             return False


#         return helper(tuple(), 0, s)
            

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin = leftmax = 0

        for char in s:
            if char == '(':
                leftmin += 1
                leftmax += 1
            elif char == ')':
                leftmin -= 1
                leftmax -= 1
            else:
                leftmin -= 1
                leftmax += 1

            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0


        if leftmin == 0:
            return True
        
        return False