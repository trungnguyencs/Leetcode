class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = {}
        self.DL = DL()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.DL.head.next.val
        
    def add(self, value: int) -> None:
        if value not in self.dic:
            self.dic[value] = self.DL.addBack(value)
        elif self.dic[value]:
            node = self.dic[value]
            self.DL.remove(node)
            self.dic[value] = None
            
class DL:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addBack(self, val):
        last = self.tail.prev
        node = Node(val, next=self.tail, prev=last)
        last.next = node
        self.tail.prev = node
        return node
    
    def remove(self, node):
        next, prev = node.next, node.prev
        prev.next = next
        next.prev = prev
        
class Node:
    
    def __init__(self, val=-1, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)