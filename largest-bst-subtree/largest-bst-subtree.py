# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        self.postOrder(root)
        return self.ans
        
    def postOrder(self, root):
        if not root: return True, float('inf'), float('-inf'), 0
        isBstLeft, lBoundLeft, rBoundLeft, sizeLeft = self.postOrder(root.left)
        isBstRight, lBoundRight, rBoundRight, sizeRight = self.postOrder(root.right)
        if isBstLeft and isBstRight and rBoundLeft < root.val < lBoundRight:
            self.ans = max(self.ans, 1 + sizeLeft + sizeRight)
            return True, min(root.val, lBoundLeft), max(root.val, rBoundRight), 1 + sizeLeft + sizeRight
        return False, -1, -1, -1