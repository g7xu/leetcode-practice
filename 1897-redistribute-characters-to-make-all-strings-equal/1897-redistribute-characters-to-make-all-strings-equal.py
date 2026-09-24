from collections import defaultdict

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        word_counts = len(words)

        char_freq = defaultdict(int)

        for word in words:
            for char in word:
                char_freq[char] += 1

        for value in char_freq.values():
            if value % word_counts != 0:
                return False

        return True