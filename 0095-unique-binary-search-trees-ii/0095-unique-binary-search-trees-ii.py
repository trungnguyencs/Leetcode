# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.backtrack(1, n)
        
    def backtrack(self, l, r):
        if l > r:
            return [None]
        ans = []
        for m in range(l, r + 1):
            leftArr = self.backtrack(l, m - 1)
            rightArr = self.backtrack(m + 1, r)
            for leftNode in leftArr:
                for rightNode in rightArr:
                    root = TreeNode(m, leftNode, rightNode)
                    ans.append(root)
        return ans