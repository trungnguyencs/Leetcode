# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.preorder(root)
        return self.ans

    def preorder(self, node):
        if node is None: return
        self.preorder(node.left)
        self.ans.append(node.val)
        self.preorder(node.right)