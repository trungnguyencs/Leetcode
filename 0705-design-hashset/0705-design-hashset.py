class MyHashSet:

    def __init__(self):
        self.hashFunc = 10**4 + 7
        self.arr = [LinkedList() for _ in range(self.hashFunc)]

    def add(self, key: int) -> None:
        L = self.arr[key % self.hashFunc]
        L.add(key)
        
    def remove(self, key: int) -> None:
        L = self.arr[key % self.hashFunc]
        L.remove(key)

    def contains(self, key: int) -> bool:
        L = self.arr[key % self.hashFunc]
        _, node = L.search(key)
        return not(node is None)
        
class Node:
    
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next
        
class LinkedList:
    
    def __init__(self):
        self.head = Node()
    
    def add(self, key):
        _, cur = self.search(key)
        if not cur:
            node = Node(key, self.head.next)
            self.head.next = node
        
    def remove(self, key):
        prev, cur = self.search(key)
        if cur:
            prev.next = prev.next.next
            
    def search(self, key):
        prev, cur = self.head, self.head.next
        while cur and cur.key != key:
            prev, cur = prev.next, cur.next
        return prev, cur

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)