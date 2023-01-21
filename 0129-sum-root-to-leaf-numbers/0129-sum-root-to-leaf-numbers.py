# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.preOrder(root, 0)
        return self.ans
    
    def preOrder(self, root, prev):
        cur = prev * 10 + root.val
        if not root.left and not root.right:
            self.ans += cur
        if root.left:
            self.preOrder(root.left, cur)
        if root.right:
            self.preOrder(root.right, cur)