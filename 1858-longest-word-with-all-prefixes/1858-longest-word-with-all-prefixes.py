class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ''
        trie = Trie()
        for word in words:
            if trie.add(word):
                ans = min([ans, word], key=lambda x: (-len(x), x))
        return ans
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        cur = self.root
        hasAllPrefixes = True
        for i, ch in enumerate(word):
            if (ch not in cur.children and i != len(word) - 1) or cur.longestWord != word[:i]:
                hasAllPrefixes = False
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.longestWord = max([cur.longestWord, word], key=len)
        return hasAllPrefixes
    
class TrieNode:
    def __init__(self):
        self.longestWord = '' #need this instead of isWord to handle case like ['ab', 'bc', 'abc']
        self.children = {}