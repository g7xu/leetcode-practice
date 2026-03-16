

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [ele for ele in s.split(" ") if ele]

        return " ".join(arr[::-1])