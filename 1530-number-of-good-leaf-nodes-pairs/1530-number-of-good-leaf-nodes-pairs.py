# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        self.postOrder(root, distance)
        return self.ans
        
    def postOrder(self, root, distance):
        if not root:
            return []
        if not root.left and not root.right:
            return [1]
        left = self.postOrder(root.left, distance)
        right = self.postOrder(root.right, distance)
        self.ans += len([(l, r) for l in left for r in right if l + r <= distance])
        return [1 + d for d in left + right]