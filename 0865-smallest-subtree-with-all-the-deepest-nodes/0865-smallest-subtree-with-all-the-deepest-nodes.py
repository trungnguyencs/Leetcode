# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #can be solved in one pass by comparing left depth and right depth
        return self.postOrder(root)[0]

    def postOrder(self, root):
        if not root: return None, 0
        left, leftDepth = self.postOrder(root.left)
        right, rightDepth = self.postOrder(root.right)
        if leftDepth > rightDepth:
            return left, leftDepth + 1
        if rightDepth > leftDepth:
            return right, rightDepth + 1
        return root, leftDepth + 1