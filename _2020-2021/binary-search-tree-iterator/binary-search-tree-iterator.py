# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.addLeft(root)
        
    def next(self) -> int:
        cur = self.stack.pop()
        if cur.right:
            self.addLeft(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0

    def addLeft(self, root):
        while root:
            self.stack.append(root)
            root = root.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()