# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dic = {num: i for i, num in enumerate(inorder)}
        return self.helper(preorder[::-1], dic, 0, len(preorder)-1)
    
    def helper(self, preorder, dic, l, r):
        if l > r: return None
        val = preorder.pop()
        i = dic[val]
        return TreeNode(val, self.helper(preorder, dic, l, i-1), self.helper(preorder, dic, i+1, r))