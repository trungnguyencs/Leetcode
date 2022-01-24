# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2 or root1.val != root2.val: return False
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
