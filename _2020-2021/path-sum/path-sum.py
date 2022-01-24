# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        self.ans = False
        self.helper(root, 0, target)
        return self.ans
        
    def helper(self, root, s, target):
        if not root: return
        s += root.val
        if not root.left and not root.right and s == target:
            self.ans = True
            return
        self.helper(root.left, s, target)
        self.helper(root.right, s, target)
