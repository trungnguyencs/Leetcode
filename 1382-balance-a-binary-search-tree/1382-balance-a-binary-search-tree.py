# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sortedArr = []
        self.inorder(root)
        return self.sortedArrToBalancedBST(self.sortedArr, 0, len(self.sortedArr) - 1)
        
    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.sortedArr.append(root)
        self.inorder(root.right)
        
    def sortedArrToBalancedBST(self, arr, l, r):
        if l > r: return None
        m = (l + r)//2
        root = arr[m]
        root.left = self.sortedArrToBalancedBST(arr, l, m - 1)
        root.right = self.sortedArrToBalancedBST(arr, m + 1, r)
        return root