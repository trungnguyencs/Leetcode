# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')
        self.postorder(root)
        return self.maxPath

    def postorder(self, root):
        if not root: return 0
        L = self.postorder(root.left)
        R = self.postorder(root.right)
        self.maxPath = max(self.maxPath, 
                            root.val,
                            root.val + L,
                            root.val + R,
                            root.val + L + R)
        return max(root.val, root.val + L, root.val + R)