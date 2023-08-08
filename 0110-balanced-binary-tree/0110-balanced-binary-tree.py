# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.postOrder(root)[0]
    
    def postOrder(self, root):
        if not root: return True, 0
        isLeftBalanced, leftHeight = self.postOrder(root.left)
        isRightBalanced, rightHeight = self.postOrder(root.right)
        if not isLeftBalanced or not isRightBalanced or abs(leftHeight - rightHeight) > 1: return False, None
        return True, 1 + max(leftHeight, rightHeight)