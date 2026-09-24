class Solution:
    def firstUniqChar(self, s: str) -> int:
        non_repeat = set()
        repeat = set()
        for char in s:
            if char not in non_repeat and char not in repeat:
                non_repeat.add(char)
            elif char in non_repeat:
                non_repeat.remove(char)
                repeat.add(char)

        for i in range(len(s)):
            if s[i] in non_repeat:
                return i

        return -1
