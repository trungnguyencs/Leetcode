# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        return self.helper(nums, 0, len(nums))
        
    def helper(self, nums, l, r):
        if r == l: return None
        m = (l + r)//2
        root = TreeNode(nums[m], self.helper(nums, l, m), self.helper(nums, m+1, r))
        return root
