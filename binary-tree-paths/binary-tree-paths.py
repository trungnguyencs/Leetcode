# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        paths = []
        self.dfs(root, [], paths)
        return paths
        
    def dfs(self, root, curPath, paths):
        if not root.left and not root.right:
            curPath.append(str(root.val))
            paths.append('->'.join(curPath))
            return
        curPath.append(str(root.val))
        if root.left:
            self.dfs(root.left, curPath, paths)
            curPath.pop()
        if root.right:
            self.dfs(root.right, curPath, paths)
            curPath.pop()
            