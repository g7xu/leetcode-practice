class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {n}

        def find_sum(num):
            total = 0
            while num > 0:
                total += (num % 10) ** 2
                num = num // 10

            return total

        while n != 1:
            n = find_sum(n)
            if n in visited:
                return False
            visited.add(n)

        return True
            