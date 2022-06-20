class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.add(word[::-1])
        return sum([length + 1 for node, length in trie.endNodes if not node.children])
                 
class Trie:
    def __init__(self):
        self.root = Node()
        self.endNodes = set()
        
    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        self.endNodes.add((node, len(word)))
        
class Node():
    def __init__(self):
        self.children = {}