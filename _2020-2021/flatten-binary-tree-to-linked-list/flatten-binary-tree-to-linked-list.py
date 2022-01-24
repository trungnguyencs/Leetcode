# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        node, tail = root, root.right
        node.left, node.right = None, self.flatten(node.left)
        while node.right: node = node.right
        node.right = self.flatten(tail)
        return root