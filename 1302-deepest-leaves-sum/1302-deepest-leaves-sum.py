# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            levelSum = 0
            for _ in range(len(q)):
                cur = q.popleft()
                levelSum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return levelSum