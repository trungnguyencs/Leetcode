from sortedcontainers import SortedDict

class MaxStack:

    def __init__(self):
        self.dic = SortedDict()
        self.DL = DL()

    def push(self, x: int) -> None:
        node = Node(x)
        self.DL.addBack(node)
        if x not in self.dic:
            self.dic[x] = []
        self.dic[x].append(node)

    def pop(self) -> int:
        node = self.DL.tail.prev
        self.DL.remove(self.dic[node.val].pop())
        if not self.dic[node.val]:
            del self.dic[node.val]
        return node.val

    def top(self) -> int:
        return self.DL.tail.prev.val

    def peekMax(self) -> int:
        maxKey, nodeList = self.dic.peekitem()
        return maxKey

    def popMax(self) -> int:
        maxVal = self.peekMax()
        self.DL.remove(self.dic[maxVal].pop())
        if not self.dic[maxVal]:
            del self.dic[maxVal]
        return maxVal
        
class Node:
    
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
        
class DL:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addBack(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node
        
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()