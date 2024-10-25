class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        return [path for path in folder if trie.addIfParentNotExists(path)]         
            
class Trie:
    def __init__(self):
        self.root = Node()
        
    def addIfParentNotExists(self, path):
        cur = self.root
        for c in path.split('/'):
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            if cur.isEnd: return False
        cur.isEnd = True
        return True
        
class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False