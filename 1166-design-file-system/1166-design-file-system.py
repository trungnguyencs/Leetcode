class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, val: int) -> bool:
        return self.trie.add(self.processPath(path), val)

    def get(self, path: str) -> int:
        return self.trie.search(self.processPath(path))
        
    def processPath(self, path):
        return path.strip('/').split('/')
    
class Node:
    
    def __init__(self, val=None):
        self.children = {}
        self.val = val
        
class Trie:
    
    def __init__(self):
        self.root = Node()
    
    def add(self, dirs, val):
        cur = self.root
        for d in dirs[:-1]:
            if d not in cur.children: return False
            cur = cur.children[d]
        if dirs[-1] in cur.children: return False
        cur.children[dirs[-1]] = Node(val)
        return True
    
    def search(self, dirs):
        cur = self.root
        for d in dirs:
            if d not in cur.children: return -1
            cur = cur.children[d]
        return cur.val
        
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)