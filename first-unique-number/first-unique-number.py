class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = {}
        self.dl = DL()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.dl.head.next.val

    def add(self, val: int) -> None:
        if val not in self.dic:
            node = Node(val)
            self.dic[val] = node
            self.dl.addBack(node)
        elif self.dic[val]:
            self.dl.remove(self.dic[val])
            self.dic[val] = None
            
class Node:
    
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DL:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, prev=self.head)
        self.head.next = self.tail
        
    def addBack(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)