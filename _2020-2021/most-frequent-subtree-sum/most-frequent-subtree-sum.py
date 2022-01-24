# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = defaultdict(int)
        self.maxFreq = 0
        self.postorder(root)
        return [k for k in self.dic if self.dic[k] == self.maxFreq]
        
    def postorder(self, root):
        if not root: return 0
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        s = left + right + root.val
        self.dic[s] += 1
        self.maxFreq = max(self.maxFreq, self.dic[s])
        return s