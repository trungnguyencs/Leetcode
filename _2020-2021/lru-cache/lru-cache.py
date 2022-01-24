class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.DL = DL()
        self.dic = {}
        
    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        val = self.dic[key].val
        self.remove(key)
        self.put(key, val)
        return val
        
    def put(self, key: int, val: int) -> None:
        if self.DL.length == self.capacity and key not in self.dic:
            self.remove(self.DL.tail.prev.key)
        if key in self.dic:
            self.remove(key)
        node = Node(key, val)
        self.DL.addFront(node)
        self.dic[key] = node
        
    def remove(self, key):
        self.DL.remove(self.dic[key])
        del self.dic[key]
        
class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class DL:
    
    def __init__(self):
        self.length = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addFront(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        self.length += 1
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)