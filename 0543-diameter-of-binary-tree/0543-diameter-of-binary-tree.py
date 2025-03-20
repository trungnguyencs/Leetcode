# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.postorder(root)
        return self.ans

    def postorder(self, root):
        if not root: return 0
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        self.ans = max(self.ans, left + right)
        return 1 + max(left, right)