class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = {}
        self.DL = DL()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.DL.head.next.val

    def add(self, val: int) -> None:
        if val in self.dic:
            if self.dic[val]:
                self.DL.remove(self.dic[val])
                self.dic[val] = None
        else:
            self.dic[val] = self.DL.addback(val)
        
class DL:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def addback(self, val):
        node = Node(val, self.tail, self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        return node
        
class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)