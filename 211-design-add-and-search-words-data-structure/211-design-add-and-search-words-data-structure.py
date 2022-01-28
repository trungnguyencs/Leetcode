class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)
    
    def dfs(self, word, i, node):
        if i == len(word):
            return node.isWord
        if word[i] in node.children:
            return self.dfs(word, i + 1, node.children[word[i]])
        if word[i] == '.':
            for ch in node.children:
                if self.dfs(word, i + 1, node.children[ch]):
                    return True
        return False
        
class Node:
    def __init__(self):
        self.isWord = False
        self.children = {}

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)