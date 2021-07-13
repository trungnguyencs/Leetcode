# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.dic = defaultdict(list)
        self.postOrder(root)
        return [self.dic[depth] for depth in range(1, len(self.dic) + 1)]
            
    def postOrder(self, root):
        if not root: return 0
        reversedDepth = 1 + max(self.postOrder(root.left), self.postOrder(root.right))
        self.dic[reversedDepth].append(root.val)
        return reversedDepth