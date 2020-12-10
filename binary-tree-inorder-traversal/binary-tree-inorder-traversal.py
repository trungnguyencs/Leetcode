# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, self.stack = [], []
        self.addLeft(root)
        while self.stack:
            cur = self.stack.pop()
            ans.append(cur.val)
            if cur.right:
                self.addLeft(cur.right)
        return ans
        
    def addLeft(self, cur):
        while cur:
            self.stack.append(cur)
            cur = cur.left
