# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        q = deque([root])
        while q:
            maxRow = -math.inf
            for _ in range(len(q)):
                cur = q.popleft()
                maxRow = max(maxRow, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(maxRow)
        return ans