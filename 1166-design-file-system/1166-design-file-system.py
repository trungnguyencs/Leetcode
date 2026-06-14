class FileSystem:

    def __init__(self):
        self.root = Node(0)

    def createPath(self, path: str, value: int) -> bool:
        folders = self.splitPath(path)
        cur = self.root
        for i, folder in enumerate(folders):
            if i == len(folders) - 1:
                if folder in cur.children:
                    return False
                cur.children[folder] = Node(value)
            else:
                if folder not in cur.children:
                    return False
                cur = cur.children[folder]
        return True

    def get(self, path: str) -> int:
        folders = self.splitPath(path)
        cur = self.root
        for folder in folders:
            if folder not in cur.children:
                return -1
            cur = cur.children[folder]
        return cur.val

    def splitPath(self, path):
        return path.split('/')[1:]

class Node:

    def __init__(self, val):
        self.val = val
        self.children = {}


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)