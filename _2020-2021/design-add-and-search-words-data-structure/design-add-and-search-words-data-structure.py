class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children: node.children[ch] = Node()
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
    
    def dfs(self, node, word, i):
        if i == len(word): return node.isWord
        ch = word[i]
        if ch != '.':
            if ch not in node.children: return False
            return self.dfs(node.children[ch], word, i+1)
        for nxt in node.children:
            if self.dfs(node.children[nxt], word, i+1): return True
        return False
        
class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)