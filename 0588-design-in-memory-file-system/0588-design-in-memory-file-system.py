class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        cur = self._traverse(path)
        return [cur.name] if cur.type == "file" else sorted(cur.children.keys())

    def mkdir(self, path: str) -> None:
        cur = self.root
        arr = self._splitPath(path)
        for name in arr:
            if name not in cur.children:
                cur.children[name] = Node(name=name)
            cur = cur.children[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        cur = self._traverse(filePath)
        cur.type = 'file'
        cur.content += content
        
    def readContentFromFile(self, filePath: str) -> str:
        cur = self._traverse(filePath)
        return cur.content
    
    def _splitPath(self, path):
        if path == '/': return []
        return path.strip('/').split('/')
    
    def _traverse(self, path):
        cur = self.root
        arr = self._splitPath(path)
        for name in arr:
            cur = cur.children[name]
        return cur        
        
class Node:
    
    def __init__(self, type='folder', name=''):
        self.name = name
        self.type = type
        self.content = ''
        self.children = defaultdict(Node)
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)