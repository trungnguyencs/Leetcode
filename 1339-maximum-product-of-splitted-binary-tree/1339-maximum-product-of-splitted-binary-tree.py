# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.maxProd = float('-inf')
        self.postOrder(root)
        self.sumOfAllNodes = root.val
        self.preOrder(root)
        return self.maxProd % (10**9 + 7)
    
    def postOrder(self, root):
        if not root: return 0
        if not root.left and not root.right: return root.val
        left, right = self.postOrder(root.left), self.postOrder(root.right)
        root.val += left + right
        return root.val
    
    def preOrder(self, root):
        if root.left:
            self.maxProd = max(self.maxProd, (self.sumOfAllNodes - root.left.val)*root.left.val)
            self.preOrder(root.left)
        if root.right:
            self.maxProd = max(self.maxProd, (self.sumOfAllNodes - root.right.val)*root.right.val)
            self.preOrder(root.right)