# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.ans = None
        self.inOrder(root)
        return self.ans
    
    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.k -= 1
        if self.k == 0:
            self.ans = root.val
            return
        self.inOrder(root.right)