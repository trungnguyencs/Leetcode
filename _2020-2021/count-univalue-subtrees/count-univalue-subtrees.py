# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.postOrder(root)
        return self.ans
    
    def postOrder(self, root):
        isLeftUnivalue = self.postOrder(root.left) and root.val == root.left.val if root.left else True
        isRightUnivalue = self.postOrder(root.right) and root.val == root.right.val if root.right else True
        ret = isLeftUnivalue and isRightUnivalue
        if ret: self.ans += 1
        return ret