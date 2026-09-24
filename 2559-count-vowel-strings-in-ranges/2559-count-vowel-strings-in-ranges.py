class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWEL = ['a', 'e', 'i', 'o', 'u']

        prefix_vowels = [0]

        for word in words:
            if word[0] in VOWEL and word[-1] in VOWEL:
                prefix_vowels.append(prefix_vowels[-1] + 1)
            else:
                prefix_vowels.append(prefix_vowels[-1])

        # prefix_vowels = prefix_vowels + [prefix_vowels[-1]]
        print(prefix_vowels)

        res = []
        for a, b in queries:
            res.append(prefix_vowels[b + 1] - prefix_vowels[a])

        return res
