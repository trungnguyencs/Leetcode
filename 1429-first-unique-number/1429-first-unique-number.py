class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dic = {}
        self.DL = DL()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.DL.head.next.val

    def add(self, val: int) -> None:
        if val not in self.dic:
            node = Node(val)
            self.dic[val] = node
            self.DL.addBack(node)
        elif self.dic[val] is not None:
            self.DL.remove(self.dic[val])
            self.dic[val] = None

class DL:

    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def addBack(self, node):
        prev = self.tail.prev
        node.next = self.tail
        node.prev = prev
        prev.next = node
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
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