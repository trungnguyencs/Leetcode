# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [], []
        self.addLeft(stack, root)
        while stack:
            root = stack.pop()
            ans.append(root.val)
            self.addLeft(stack, root.right)
        return ans
    
    def addLeft(self, stack, root):
        while root:
            stack.append(root)
            root = root.left