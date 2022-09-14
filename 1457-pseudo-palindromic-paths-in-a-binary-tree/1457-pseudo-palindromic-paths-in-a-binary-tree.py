# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.preOrder(root, Counter())
        return self.ans
        
    def preOrder(self, root, counter):
        if not root: return
        counter[root.val] += 1
        if not root.left and not root.right:
            if len([x for x in counter.values() if x % 2 == 1]) <= 1:
                self.ans += 1
            counter[root.val] -= 1
            return
        self.preOrder(root.left, counter)
        self.preOrder(root.right, counter)
        counter[root.val] -= 1