# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.preOrderArr = []
        self.p = -1
        self.addLeft(root)

    def hasNext(self) -> bool:
        return self.p < len(self.preOrderArr) - 1 or len(self.stack) != 0

    def next(self) -> int:
        if self.p == len(self.preOrderArr) - 1:
            node = self.stack.pop()
            self.addLeft(node.right)
            self.preOrderArr.append(node.val)
        self.p += 1
        return self.preOrderArr[self.p]

    def hasPrev(self) -> bool:
        return self.p > 0

    def prev(self) -> int:
        self.p -= 1
        return self.preOrderArr[self.p]
        
    def addLeft(self, root):
        while root:
            self.stack.append(root)
            root = root.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()