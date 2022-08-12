# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        m, M = min(p.val, q.val), max(p.val, q.val)
        while root.val < m or root.val > M:
            if root.val < m: root = root.right
            if root.val > M: root = root.left
        return root