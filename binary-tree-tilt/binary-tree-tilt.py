# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.diff = 0
        self.postorder(root)
        return self.diff
    
    def postorder(self, root):
        if not root: return 0
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        self.diff += abs(left - right)
        return root.val + left + right