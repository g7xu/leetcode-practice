# monotonically increaseing stack

# 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = len(heights) * min(heights)
        mon_increase_stack = [(-1, -1)]
        
        for i in range(len(heights)):
            h = heights[i]
            if mon_increase_stack[-1][0] < h:
                mon_increase_stack.append((h, i))
            else:
                while mon_increase_stack[-1][0] >= h:
                    pro_h, pro_idx = mon_increase_stack.pop()
                    res = max(res, (i - mon_increase_stack[-1][1] - 1) * pro_h)
                mon_increase_stack.append((h, i))
        
        # print(mon_increase_stack)
        for i in range(1, len(mon_increase_stack)):
            w = mon_increase_stack[-1][-1] - mon_increase_stack[i-1][-1]
            h = mon_increase_stack[i][0]
            res = max(res, (w) * h)

        return res


