# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.helper(root, TreeNode())
        return self.ans
        
    def helper(self, root, parent):
        if not root: return
        if not root.left and not root.right:
            if root is parent.left:
                self.ans += root.val
            return
        self.helper(root.left, root)
        self.helper(root.right, root)