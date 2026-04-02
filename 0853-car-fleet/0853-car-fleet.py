class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        status = sorted([[p, s] for p, s in zip(position, speed)])

        hr = [(target - p) / s for p, s in status]

        stack = []

        for i in range(len(hr) - 1, -1, -1):
            if not stack or stack[-1] < hr[i]:
                stack.append(hr[i])

        return len(stack)