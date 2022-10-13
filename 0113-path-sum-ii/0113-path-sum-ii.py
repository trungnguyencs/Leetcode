# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        self.ans = []
        self.preorder(root, [], target)
        return self.ans
    
    def preorder(self, root, path, target):
        if not root: return
        path.append(root.val)
        if not root.left and not root.right and root.val == target:
            self.ans.append(path[:])
        if root.left:
            self.preorder(root.left, path, target - root.val)
        if root.right:
            self.preorder(root.right, path, target - root.val)
        path.pop()