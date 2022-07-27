# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        head, tail = root, root.right
        root.left, root.right = None, self.flatten(root.left)
        while head.right:
            head = head.right
        head.right = self.flatten(tail)
        return root