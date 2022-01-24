# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:
            node = p.right
            while node.left: node = node.left
            return node
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor