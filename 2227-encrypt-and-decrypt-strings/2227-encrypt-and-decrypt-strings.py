class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word)
        self.k2V = {}
        self.v2K = defaultdict(set)
        for k, v in zip(keys, values):
            self.k2V[k] = v
            self.v2K[v].add(k)

    def encrypt(self, word1: str) -> str:
        return ''.join([self.k2V[k] for k in word1])

    def decrypt(self, word2: str) -> int:
        return self.helper(word2, 0, self.trie.root)
        
    def helper(self, word2, i, node):
        if i == len(word2):
            return 1 if node.isWord else 0
        ans = 0
        v = word2[i:i+2]
        for k in self.v2K[v]:
            if k in node.children:
                ans += self.helper(word2, i+2, node.children[k])
        return ans
                
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.isWord = True
        
class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)