class Solution:
    def suggestedProducts(self, words: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in sorted(words):
            trie.add(word)
        return trie.suggest(searchWord)
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
            if len(node.topThree) < 3:
                node.topThree.append(word)
                
    def suggest(self, word):
        ans = [[]]*len(word)
        node = self.root
        for i, ch in enumerate(word):
            if ch in node.children:
                node = node.children[ch]
                ans[i] = node.topThree
            else:
                break
        return ans
            
class Node:
    def __init__(self):
        self.children = {}
        self.topThree = []