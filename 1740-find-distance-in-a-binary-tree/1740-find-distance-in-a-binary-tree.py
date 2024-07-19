# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q: return 0
        self.ans = -1
        self.postOrder(root, p, q)
        return self.ans
        
    def postOrder(self, root, p, q):
        if not root: return 0
        left = self.postOrder(root.left, p, q)
        right = self.postOrder(root.right, p, q)
        if left and right:
            self.ans = left + right
            return
        if root.val in [p, q]:
            if left:
                self.ans = left
                return
            if right:
                self.ans = right
                return
            return 1
        if left or right:
            return 1 + (left or right)
        return 0