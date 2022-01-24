# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        self.ans = []
        self.dfs(root, 0, [], target)
        return self.ans
    
    def dfs(self, root, curSum, path, target):
        curSum += root.val
        path.append(root.val)
        if not root.left and not root.right and curSum == target: self.ans.append(path[:])
        if root.left: self.dfs(root.left, curSum, path, target)
        if root.right: self.dfs(root.right, curSum, path, target)
        path.pop()