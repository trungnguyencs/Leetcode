# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        dummy = TreeNode(left=root)
        self.postOrder(dummy, target)
        return dummy.left
        
    def postOrder(self, root, target):
        if not root: return True
        left = self.postOrder(root.left, target)
        right = self.postOrder(root.right, target)
        if left: root.left = None
        if right: root.right = None
        if left and right and root.val == target: return True