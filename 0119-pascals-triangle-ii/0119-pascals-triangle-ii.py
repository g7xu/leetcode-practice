class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        if rowIndex == 0:
            return res

        pre = self.getRow(rowIndex - 1)
        for i in range(len(pre) - 1):
            res.append(pre[i] + pre[i + 1])

        res.append(1)

        return res