class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1

        total = 0 

        for i in range(0, n):
            # 0, 1, 2
            total += self.numTrees(i) * self.numTrees(n - i - 1)

        return total
