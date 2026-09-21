r""" Thinking area



"""

class TrieNode:
    def __init__(self, char = None):
        self.char = char
        self.children = dict()
        self.is_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
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
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return len(node.children) >= 0        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)