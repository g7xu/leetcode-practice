class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        mono_stack = []
        print(len(num))

        for i in range(len(num)):
            while mono_stack and int(mono_stack[-1]) > int(num[i]) and k > 0:
                mono_stack.pop()
                k -= 1

            mono_stack.append(num[i])


        while k > 0 and mono_stack:
            mono_stack.pop()
            k -= 1

        res = ''

        for char in mono_stack:
            if not res and char == '0':
                continue
            
            res += char 

        if not res:
            return '0'

        return res

        