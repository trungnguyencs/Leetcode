class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.list = DoublyLinkedList()
        self.capacity = capacity
        self.length = 0

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.list.remove(node)
        self.list.addFront(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.setVal(val)
            self.list.remove(node)
            self.list.addFront(node)
        else:
            #if cache is full, evict the least recently used
            if self.length == self.capacity:
                lastNode = self.list.getLastNode()
                self.list.remove(lastNode)
                del self.dic[lastNode.key]
                self.length -= 1
            newNode = ListNode(key, val)
            self.list.addFront(newNode)
            self.dic[key] = newNode
            self.length += 1
            

class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode(prev=self.head)
        self.head.next = self.tail

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def addFront(self, node):
        prev, next = self.head, self.head.next
        node.prev, node.next = prev, next
        prev.next, next.prev = node, node

    def getLastNode(self):
        return self.tail.prev

class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def setVal(self, val):
        self.val = val

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)