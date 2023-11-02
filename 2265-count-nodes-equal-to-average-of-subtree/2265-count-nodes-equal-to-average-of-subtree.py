# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.postOrder(root)
        return self.ans
        
    def postOrder(self, root):
        if not root:
            return (0, 0)
        if not root.left and not root.right:
            self.ans += 1
            return (root.val, 1)
        leftSum, leftCount = self.postOrder(root.left)
        rightSum, rightCount = self.postOrder(root.right)
        curSum, curCount = leftSum + rightSum + root.val, leftCount + rightCount + 1
        if root.val == curSum//curCount:
            self.ans += 1
        return curSum, curCount