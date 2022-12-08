# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.preOrder(root1, []) == self.preOrder(root2, [])
        
    def preOrder(self, root, arr):
        if not root: return
        if not root.left and not root.right:
            arr.append(root.val)
        if root.left:
            self.preOrder(root.left, arr)
        if root.right:
            self.preOrder(root.right, arr)
        return arr