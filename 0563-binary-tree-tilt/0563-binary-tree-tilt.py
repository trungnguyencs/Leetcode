# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.postOrder(root)
        return self.ans
        
    def postOrder(self, root):
        if not root: return 0
        leftSum = self.postOrder(root.left)
        rightSum = self.postOrder(root.right)
        self.ans += abs(leftSum - rightSum)
        return root.val + leftSum + rightSum