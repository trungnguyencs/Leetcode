# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.postOrder(root)
        
    def postOrder(self, root):
        if not root: return None
        root.left, root.right = self.postOrder(root.left), self.postOrder(root.right)
        return None if not root.left and not root.right and root.val == 0 else root