# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.dfs(root, low, high)
        return self.ans
    
    def dfs(self, root, low, high):
        if not root:
            return
        if root.val < low:
            self.dfs(root.right, low, high)
        elif root.val > high:
            self.dfs(root.left, low, high)
        else:
            self.ans += root.val
            self.dfs(root.left, low, high)
            self.dfs(root.right, low, high)