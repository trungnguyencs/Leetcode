# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.helper(root)[0]
    
    def helper(self, root):
        if not root: return None, 0
        left, leftDepth = self.helper(root.left)
        right, rightDepth = self.helper(root.right)
        if leftDepth > rightDepth: return left, leftDepth + 1     # left is deeper => return left
        if rightDepth > leftDepth: return right, rightDepth + 1    # right is deeper => return right
        return root, leftDepth + 1     # equal depth => return root