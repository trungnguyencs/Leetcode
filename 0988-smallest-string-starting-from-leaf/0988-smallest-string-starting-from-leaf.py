# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # # postOrder won't work
        # if not root: return ''
        # ch = chr(ord('a') + root.val)
        # left = self.smallestFromLeaf(root.left)
        # right = self.smallestFromLeaf(root.right)
        # if left == '': return right + ch
        # if right == '': return left + ch
        # print(left + ch, right + ch)
        # return min(left + ch, right + ch)
        
        # simply bruteforce
        if not root: return ''
        self.ans = '~' #dummy thing that is > any 'zz..z'
        self.dfs(root, '')
        return self.ans
    
    def dfs(self, root, s):
        ch = chr(ord('a') + root.val)
        s += ch
        if not root.left and not root.right:
            self.ans = min(self.ans, s[::-1])
            return
        if root.left:
            self.dfs(root.left, s)
        if root.right:
            self.dfs(root.right, s)