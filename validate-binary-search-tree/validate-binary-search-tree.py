# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
        
    def helper(self, root, lBound, rBound):
        if not root: return True
        if not lBound < root.val < rBound: return False
        return self.helper(root.left, lBound, root.val) and self.helper(root.right, root.val, rBound)