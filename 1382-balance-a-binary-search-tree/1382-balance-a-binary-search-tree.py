# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        self.inOrder(root, arr)
        return self.createBalancedBst(arr, 0, len(arr) - 1)

    def inOrder(self, root, arr):
        if not root: return
        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)

    def createBalancedBst(self, arr, l, r):
        if l > r: return None
        m = (l + r)//2
        root = TreeNode(arr[m])
        root.left = self.createBalancedBst(arr, l, m - 1)
        root.right = self.createBalancedBst(arr, m + 1, r)
        return root