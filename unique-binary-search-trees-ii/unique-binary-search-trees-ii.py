# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.dfs(range(1, n+1))
        
    def dfs(self, arr):
        if not arr: return [None]
        return [TreeNode(num, left, right)
                for i, num in enumerate(arr)
                for left in self.dfs(arr[:i])
                for right in self.dfs(arr[i+1:])
               ]