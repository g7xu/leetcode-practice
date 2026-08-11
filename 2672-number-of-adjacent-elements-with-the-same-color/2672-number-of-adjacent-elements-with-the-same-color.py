# simulation
# when throwing in
# check impact
# then check increase


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        curr = 0
        colors = [0] * n
        res = []
        for idx, color in queries:
            # check impact
            if idx >= 1 and colors[idx] != 0 and colors[idx] == colors[idx - 1]:
                curr -= 1

            if idx <= n - 2 and colors[idx] != 0 and colors[idx] == colors[idx + 1]:
                curr -= 1

            colors[idx] = color

            if idx >= 1 and colors[idx] == colors[idx - 1]:
                curr += 1

            if idx <= n - 2 and colors[idx] == colors[idx + 1]:
                curr += 1

            res.append(curr)

        return res



        