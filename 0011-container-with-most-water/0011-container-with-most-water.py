# brute force O(n^2)
# try all possible ways

# sliding window?

## shirnk
## 

## expand
## 


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = -1

        l = 0
        r = len(height) - 1

        while l < r:
            res = max(res, (r - l) * min(height[r], height[l]))

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return res