class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num in arr1:
            trie.add(str(num))
        maxPrefixLength = 0
        for num in arr2:
            maxPrefixLength = max(maxPrefixLength, trie.findLongestPrefix(str(num)))
        return maxPrefixLength
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
    
    def findLongestPrefix(self, word):
        cur = self.root
        length = 0
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
                length += 1
            else:
                break
        return length

class TrieNode:
    def __init__(self):
        self.children = {}