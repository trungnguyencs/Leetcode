class FirstUnique:
​
    def __init__(self, nums: List[int]):
        self.dl = DL()
        self.dic = defaultdict(Node)
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        return self.dl.head.next.val
​
    def add(self, num: int) -> None:
        if num not in self.dic:
            self.dic[num] = self.dl.addback(num)
        elif self.dic[num]:
            self.dl.remove(self.dic[num])
            self.dic[num] = None
            
class DL:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        # self.print()
        
    def addback(self, num):
        node = Node(val=num, next=self.tail, prev=self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        return node
        # self.print()
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        # self.print()
        
    def print(self):
        head = self.head
        arr = []
