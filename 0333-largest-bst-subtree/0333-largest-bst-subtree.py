# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.maxBst = 0
        self.postorder(root)
        return self.maxBst
    
    def postorder(self, root):
        if not root:
            return 0, float('inf'), float('-inf'), True            
        leftSize, leftMin, leftMax, leftIsBst = self.postorder(root.left)
        rightSize, rightMin, rightMax, rightIsBst = self.postorder(root.right)
        if not (leftIsBst and rightIsBst and leftMax < root.val < rightMin):
            return -1, -1, -1, False
        self.maxBst = max(self.maxBst, 1 + leftSize + rightSize)
        return 1 + leftSize + rightSize, min(root.val, leftMin), max(root.val, rightMax), True