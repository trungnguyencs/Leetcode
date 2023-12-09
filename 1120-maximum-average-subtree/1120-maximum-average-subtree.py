# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.ans = float('-inf')
        self.postOrder(root)
        return self.ans
    
    def postOrder(self, root):
        if not root: return 0, 0
        leftSum, leftCount = self.postOrder(root.left)
        rightSum, rightCount = self.postOrder(root.right)
        total, count = leftSum + rightSum + root.val, leftCount + rightCount + 1
        self.ans = max(self.ans, total/count)
        return total, count