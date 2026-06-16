class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        for ele in s:
            if ele not in ['*', '#', '%']:
                stack.append(ele)
                continue

            if not stack:
                continue
            
            if ele == '*':
                stack.pop()
            elif ele == '#':
                stack = stack + stack
            else:
                stack = stack[::-1]

        return "".join(stack)