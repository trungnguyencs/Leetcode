class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i, ch in enumerate(word):
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
            cur.childCount += 1
            if i == len(word) - 1:
                cur.selfCount += 1 

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for ch in word:
            if ch not in cur.children: return 0
            cur = cur.children[ch]
        return cur.selfCount       

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children: return 0
            cur = cur.children[ch]
        return cur.childCount 

    def erase(self, word: str) -> None:
        cur = self.root
        for i, ch in enumerate(word):
            cur.children[ch].childCount -= 1
            if cur.children[ch].childCount == 0:
                del cur.children[ch]
                return
            else:
                cur = cur.children[ch]
                if i == len(word) - 1:
                    cur.selfCount -= 1
            
class Node:
    
    def __init__(self):
        self.selfCount = 0
        self.childCount = 0
        self.children = {}


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)