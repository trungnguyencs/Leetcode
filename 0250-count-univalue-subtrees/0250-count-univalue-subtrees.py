# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.isUniversal(root)
        return self.ans
    
    def isUniversal(self, root):
        if not root: return True
        isLeftUniversal = self.isUniversal(root.left)
        isRightUniversal = self.isUniversal(root.right)
        if not (isLeftUniversal and isRightUniversal): return False 
        if root.left and root.val != root.left.val: return False
        if root.right and root.val != root.right.val: return False
        self.ans += 1
        return True