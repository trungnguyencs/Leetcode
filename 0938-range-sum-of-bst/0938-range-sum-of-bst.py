# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.inOrder(root, low, high)
        return self.ans
        
    def inOrder(self, root, low, high):
        if not root: return
        if root.val < low:
            self.inOrder(root.right, low, high)
        elif root.val > high:
            self.inOrder(root.left, low, high)
        else:
            self.inOrder(root.left, low, high)
            self.ans += root.val
            self.inOrder(root.right, low, high)