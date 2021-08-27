class FileSystem:

    def __init__(self):
        self.root = Node()
        self.cur = self.root
        
    def ls(self, path: str) -> List[str]:
        if path == '/': return sorted(self.root.children)
        self.cur = self.root
        for f in self.processPath(path):
            self.cur = self.cur.children[f]
        return [f] if self.cur.type == "file" else sorted(self.cur.children.keys())

    def mkdir(self, path: str) -> None:
        self.cur = self.root
        for f in self.processPath(path):
            if f not in self.cur.children:
                self.cur.children[f] = Node()
            self.cur = self.cur.children[f]

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.cur.type = "file"
        self.cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        self.mkdir(filePath)
        return self.cur.content
        
    def processPath(self, s):
        return s.strip('/').split('/')
    
class Node:
    
    def __init__(self):
        self.content = ''
        self.type = "folder"
        self.children = defaultdict(Node)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)