# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret, count = self.helper(root, p, q)
        return ret if count == 2 else None
    
    def helper(self, root, p, q):
        if not root: return None, 0
        left, lCount = self.helper(root.left, p, q)
        right, rCount = self.helper(root.right, p, q)
        count = lCount + rCount + (1 if root in [p, q] else 0)
        if root in [p, q] or (left and right): return root, count
        return left or right, count