# monotonicall decreasing stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        md_stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while md_stack and md_stack[-1][0] < temperatures[i]:
                res[md_stack[-1][1]] = i - md_stack[-1][1]
                md_stack.pop()

            md_stack.append((temperatures[i], i))
            
        return res