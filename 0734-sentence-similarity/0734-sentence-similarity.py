from collections import defaultdict

class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2): return False

        mapping = defaultdict(set)

        for a, b in similarPairs:
            mapping[a].add(b)
            mapping[b].add(a)

        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and word2 not in mapping[word1]:
                return False

        return True