# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.inOrder(root, arr)
        return arr[0]
    
    def inOrder(self, root, arr):
        if not root: return None
        self.inOrder(root.left, arr)
        root.left = None
        if arr:
            arr[-1].right = root
        arr.append(root)
        self.inOrder(root.right, arr)