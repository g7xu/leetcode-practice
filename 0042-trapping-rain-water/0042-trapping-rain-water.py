class Solution:
    def trap(self, height: List[int]) -> int:
        left_to_right_max = [0]

        for i in height:
            left_to_right_max.append(max(left_to_right_max[-1], i))

        left_to_right_max.pop(-1)

        right_to_left_max = [0]

        for i in range(len(height) - 1, 0, -1):
            right_to_left_max.append(max(
                right_to_left_max[-1],
                height[i]
            ))

        right_to_left_max = right_to_left_max[::-1]

        res = 0

        for i, j, b in zip(left_to_right_max, right_to_left_max, height):
            res += max(min(i, j) - b, 0)

        return res 