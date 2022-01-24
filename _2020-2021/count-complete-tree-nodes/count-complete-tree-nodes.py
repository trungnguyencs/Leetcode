# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        hL = hR = 0
        node1 = node2 = root
        while node1:
            node1 = node1.left
            hL += 1
        while node2:
            node2 = node2.right
            hR += 1
        if hL == hR: return 2**hL - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)