# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = level = 1
        q = deque([root])
        maxLevelSum = float('-inf')
        while q:
            levelSum = 0
            for _ in range(len(q)):
                cur = q.popleft()
                levelSum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if levelSum > maxLevelSum:
                maxLevelSum = levelSum
                ans = level
            level += 1
        return ans