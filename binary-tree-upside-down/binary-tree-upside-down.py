# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left: return root
        prev, cur, prevRight = None, root, None
        while cur:
            nxt = cur.left
            cur.left = prevRight
            prevRight = cur.right
            cur.right = prev
            prev, cur = cur, nxt
        return prev