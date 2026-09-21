r""" Thinking area



"""
class TrieNode:

    def __init__(self):
        self.children = dict()
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True
        
    def helper(self, node, word, idx):
        if idx == len(word):
            return node.is_word

        if word[idx] == '.':
            return any([self.helper(next_node, word, idx + 1) for next_node in node.children.values()])

        if word[idx] not in node.children:
            return False

        return self.helper(node.children[word[idx]], word, idx + 1)


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.helper(self.root, word, 0)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)