# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, node, s):
        s = s*10 + node.val
        if not node.left and not node.right:
            self.ans += s
            return
        if node.left: self.dfs(node.left, s)
        if node.right: self.dfs(node.right, s)