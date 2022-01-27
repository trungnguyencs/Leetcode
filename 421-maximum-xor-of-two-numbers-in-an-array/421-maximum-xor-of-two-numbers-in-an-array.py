class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.addNum(num)
        maxXor = 0
        for num in nums:
            maxXor = max(maxXor, trie.findMaxXor(num))
        return maxXor
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def addNum(self, num):
        cur = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in cur.children:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            
    def findMaxXor(self, num):
        cur = self.root
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if 1 - bit in cur.children:
                xor += (1 << i)
                cur = cur.children[1 - bit]
            else:
                cur = cur.children[bit]
        return xor        

class Node:
    def __init__(self):
        self.children = {}