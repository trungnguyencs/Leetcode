# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.closest = float('inf')
        self.helper(root, target)
        return self.closest
    
    def helper(self, root, target):
        if not root: return
        if abs(root.val - target) < abs(self.closest - target):
            self.closest = root.val
        if root.val > target:
            self.helper(root.left, target)
        elif root.val < target:
            self.helper(root.right, target)