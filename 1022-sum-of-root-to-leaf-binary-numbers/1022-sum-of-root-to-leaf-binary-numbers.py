# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.preorder(root, 0)
        return self.ans
        
    def preorder(self, root, val):
        val = val*2 + root.val
        if not root.left and not root.right:
            self.ans += val
            return
        if root.left:
            self.preorder(root.left, val)
        if root.right:
            self.preorder(root.right, val)