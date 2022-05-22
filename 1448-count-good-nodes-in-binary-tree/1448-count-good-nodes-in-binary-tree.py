# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, root.val)
        return self.ans
    
    def dfs(self, node, maxVal):
        if not node: return
        if node.val >= maxVal:
            self.ans += 1
            maxVal = node.val
        self.dfs(node.left, maxVal)
        self.dfs(node.right, maxVal)