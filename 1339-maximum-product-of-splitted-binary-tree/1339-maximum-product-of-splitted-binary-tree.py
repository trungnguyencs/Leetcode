# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.sum = 0
        self.sum = self.getSum(root) #1st pass to get the sum of all nodes
        self.getSum(root) #2nd pass to update self.ans
        return self.ans % (10**9 + 7)

    def getSum(self, root):
        if not root: return 0
        left = self.getSum(root.left)
        right = self.getSum(root.right)
        self.ans = max(self.ans, left * (self.sum - left), right * (self.sum - right))
        return left + right + root.val