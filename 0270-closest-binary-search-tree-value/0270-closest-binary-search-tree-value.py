# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        minDiff = abs(root.val - target)
        while root:
            if abs(root.val - target) < minDiff or (abs(root.val - target) == minDiff and root.val < ans):
                minDiff = abs(root.val - target)
                ans = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return ans