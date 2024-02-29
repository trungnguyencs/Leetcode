# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.postOrder(root)
        return self.ans
        
    def postOrder(self, root):
        if not root: return 0
        leftSum = self.postOrder(root.left)
        rightSum = self.postOrder(root.right)
        if root.val == leftSum + rightSum:
            self.ans += 1
        return root.val + leftSum + rightSum