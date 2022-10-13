# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums) - 1)
        
    def helper(self, nums, l, r):
        if l > r: return None
        if l == r: return TreeNode(val=nums[l])
        m = (l + r)//2
        return TreeNode(val=nums[m], left=self.helper(nums, l, m - 1), right = self.helper(nums, m + 1, r))