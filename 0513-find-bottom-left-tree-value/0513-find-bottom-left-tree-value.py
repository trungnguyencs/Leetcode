# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # BFS solution is easy
        return self.postOrder(root)[0]
    
    def postOrder(self, root):
        if not root: return None, 0
        if not root.left and not root.right: return root.val, 1
        leftLeaf, leftHeight = self.postOrder(root.left)
        rightLeaf, rightHeight = self.postOrder(root.right)
        if rightHeight > leftHeight: return rightLeaf, 1 + rightHeight
        return leftLeaf, 1 + leftHeight