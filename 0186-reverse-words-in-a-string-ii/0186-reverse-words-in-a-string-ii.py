class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l, i1, i2):
            while i1 < i2:
                s[i1], s[i2] = s[i2], s[i1]
                i1 += 1
                i2 -= 1

        reverse(s, 0, len(s) - 1)

        i1 = i2 = 0
        while i2 < len(s):

            if i2 == len(s) - 1 or s[i2 + 1] == ' ':
                reverse(s, i1, i2)
                i1 = i2 = i2 + 2
                continue

            i2 += 1

            





