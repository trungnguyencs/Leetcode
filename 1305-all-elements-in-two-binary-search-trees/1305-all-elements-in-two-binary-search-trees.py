# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1, arr2 = [], []
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        return self.merge(arr1, arr2)
        
    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)
    
    def merge(self, arr1, arr2):
        ans = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        while i < len(arr1):
            ans.append(arr1[i])
            i += 1
        while j < len(arr2):
            ans.append(arr2[j])
            j += 1
        return ans