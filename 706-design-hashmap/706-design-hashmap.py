class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashFunc = 10**4 + 7
        self.arr = [LinkedList() for _ in range(self.hashFunc)]
        
    def put(self, key: int, val: int) -> None:
        """
        value will always be non-negative.
        """
        L = self.arr[key % self.hashFunc]
        _, node = L.search(key)
        if node: node.val = val
        else: L.addFront(Node(key, val))
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        L = self.arr[key % self.hashFunc]
        _, node = L.search(key)
        return node.val if node else -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        L = self.arr[key % self.hashFunc]
        L.remove(key)
        
class LinkedList:
    
    def __init__(self):
        self.head = Node()
        
    def addFront(self, node):
        node.next = self.head.next
        self.head.next = node
    
    def search(self, key):
        prev, cur = self.head, self.head.next
        while cur and cur.key != key:
            cur = cur.next
            prev = prev.next
        return prev, cur
    
    def remove(self, key):
        prev, cur = self.search(key)
        if cur: prev.next = cur.next

class Node:
    
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next  


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)