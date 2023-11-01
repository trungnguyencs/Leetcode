# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.maxFreq = self.freq = 0
        self.curVal = root.val
        self.inOrder(root)
        return self.ans
    
    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        if root.val == self.curVal:
            self.freq += 1
        else:
            self.curVal = root.val
            self.freq = 1
        if self.freq == self.maxFreq:
            self.ans.append(root.val)
        elif self.freq > self.maxFreq:
            self.maxFreq = self.freq
            self.ans = [root.val]
        self.inOrder(root.right)