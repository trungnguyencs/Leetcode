# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.preorder(root)
        return self.ans
    
    def preorder(self, root):
        if not root: return
        if root.left:
            if not root.right:
                self.ans.append(root.left.val)
            self.preorder(root.left)
        if root.right:
            if not root.left:
                self.ans.append(root.right.val)
            self.preorder(root.right)