class Solution:
    def isValid(self, s: str) -> bool:
        s_stack = []

        for i in s:
            if i in '({[':
                s_stack.append(i)
            else:
                if len(s_stack) == 0:
                    return False
                
                if i == ')':
                    if s_stack[-1] == "(":
                        s_stack.pop()
                    else:
                        return False
                elif i == "}":
                    if s_stack[-1] == "{":
                        s_stack.pop()
                    else:
                        return False
                else:
                    if s_stack[-1] == "[":
                        s_stack.pop()
                    else:
                        return False

        if len(s_stack) == 0:
            return True
        
        return False