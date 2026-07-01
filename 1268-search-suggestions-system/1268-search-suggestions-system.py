class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for p in products:
            trie.add(p)
        ans = []
        cur = trie.root
        for ch in searchWord:
            if ch not in cur.children: break
            cur = cur.children[ch]
            ans.append(cur.minThree)
        return ans + [[] for _ in range(len(searchWord) - len(ans))]

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
            if len(cur.minThree) < 3:
                cur.minThree.append(word)
        cur.isWord = True

class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.minThree = []
