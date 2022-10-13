# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 0
        q = deque([(root, 0)])
        while q:
            maxWidth = max(maxWidth, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                cur, position = q.popleft()
                if cur.left:
                    q.append((cur.left, 2*position))
                if cur.right:
                    q.append((cur.right, 2*position + 1))
        return maxWidth