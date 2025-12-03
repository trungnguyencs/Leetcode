# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        nodeSet1 = set()
        nodeSet2 = set()
        self.dfs(root1, nodeSet1)
        self.dfs(root2, nodeSet2)
        return any(target - val1 in nodeSet2 for val1 in nodeSet1)
    
    def dfs(self, root, nodeSet):
        if not root: return
        nodeSet.add(root.val)
        self.dfs(root.left, nodeSet)
        self.dfs(root.right, nodeSet)       