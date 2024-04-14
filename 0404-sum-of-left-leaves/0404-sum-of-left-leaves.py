# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, isLeft=False)
        return self.ans
    
    def dfs(self, root, isLeft):
        if not root:
            return 0
        if not root.left and not root.right and isLeft:
            self.ans += root.val
        if root.left:
            self.dfs(root.left, True)
        if root.right:
            self.dfs(root.right, False)