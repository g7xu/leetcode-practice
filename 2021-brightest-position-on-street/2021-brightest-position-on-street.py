class Solution:
    def brightestPosition(self, lights: list[list[int]]) -> int:
        arr = []

        for po, r in lights:
            arr += [(po - r, 1), (po + r + 1, -1)]

        res = 0
        res_b = -1
        cur_b = 0
        for p, c in sorted(arr):
            # print(p, c)

            cur_b += c
            # print(cur_b, p)

            if cur_b > res_b:
                res_b = cur_b
                res = p

        return res

            


