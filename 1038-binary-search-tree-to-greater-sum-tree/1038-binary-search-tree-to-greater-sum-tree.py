# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     # Solution 1:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         self.total = self.postOrder(root)
#         self.curSum = 0
#         self.inOrder(root)
#         return root
        
#     def postOrder(self, root):
#         if not root: return 0
#         return root.val + self.postOrder(root.left) + self.postOrder(root.right)
    
#     def inOrder(self, root):
#         if not root: return
#         self.inOrder(root.left)
#         root.val, self.curSum = self.total - self.curSum, self.curSum + root.val
#         self.inOrder(root.right)

    # Solution 2:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.curSum = 0
        self.reversedInOrder(root)
        return root
    
    def reversedInOrder(self, root):
        if not root: return
        self.reversedInOrder(root.right)
        self.curSum += root.val
        root.val = self.curSum
        self.reversedInOrder(root.left)