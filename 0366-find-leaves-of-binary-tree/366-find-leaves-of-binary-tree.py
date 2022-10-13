# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        self.postOrder(root, dic)
        return [dic[level] for level in sorted(dic.keys())]
        
    def postOrder(self, root, dic):
        if not root: return 0
        left, right = self.postOrder(root.left, dic), self.postOrder(root.right, dic)
        reversedLevel = 1 + max(left, right)
        dic[reversedLevel].append(root.val)
        return reversedLevel