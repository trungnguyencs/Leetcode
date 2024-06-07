class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.trie = Trie(dictionary)
        return ' '.join(self.trie.findPrefix(w) for w in sentence.split())
        
class Trie:
    def __init__(self, words):
        self.root = Node()
        for w in words:
            self.addWord(w)
    
    def addWord(self, w):
        cur = self.root
        for ch in w:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isWord = True
        
    def findPrefix(self, word):
        prefix = []
        cur = self.root
        for ch in word:
            if ch in cur.children:
                prefix.append(ch)
                cur = cur.children[ch]
                if cur.isWord:
                    return ''.join(prefix)
            else: break
        return word
    
class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False