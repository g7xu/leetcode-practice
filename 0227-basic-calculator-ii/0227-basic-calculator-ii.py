r""" Thinking area



"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        p = 0
        while p < len(s):
            # finding block
            if s[p] in ['/', '*', '+', '-']:
                stack.append(s[p])
                p += 1
                continue

            if s[p] == ' ':
                p += 1
                continue

            num = ''
            while p < len(s) and s[p].isdigit():
                num += s[p]
                p += 1
            num = int(num)

            if stack and stack[-1] in ['/', '*']:
                prev_o = stack.pop()
                prev = stack.pop()
            
                if prev_o == '/':
                    tmp = prev // num
                else:
                    tmp = prev * num

                stack.append(tmp)
            else:
                stack.append(num)

            

        res = stack[0]
        # print(stack)
        for i in range(1, len(stack), 2):
            if stack[i] == '+':
                res += stack[i + 1]
            else:
                res -= stack[i + 1]

        return res

            