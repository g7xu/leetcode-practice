class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
                continue

            if stack[-1] + char in ['AB', 'CD']:
                stack.pop()
            else:
                stack.append(char)

        return len(stack)