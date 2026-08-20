

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        @cache
        def good(distance, position, m):
            prev_ball_pos = position[0]
            ball_placed = 1

            for i in range(1, len(position)):
                curr_pos = position[i]
                if curr_pos - prev_ball_pos >= distance:
                    ball_placed += 1
                    prev_ball_pos = curr_pos

                if ball_placed == m:
                    return True

            return False

        
        
        position = tuple(sorted(position))
        left, right = 1, (position[-1]) // (m -1)

        while left < right - 1:
            mid = (left + right) // 2

            print(mid)
            if good(mid, position, m):
                left = mid
            else:
                right = mid - 1

        # print(right, left)
        if good(right, position, m):
            return right
        
        return left
