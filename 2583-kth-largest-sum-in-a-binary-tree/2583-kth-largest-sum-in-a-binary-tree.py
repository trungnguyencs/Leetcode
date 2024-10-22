# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
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
            if len(heap) < k:
                heappush(heap, levelSum)
            elif levelSum > heap[0]:
                heapreplace(heap, levelSum)
        return -1 if len(heap) < k else heap[0]