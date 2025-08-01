# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: return []
        offset = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            cur, d = q.popleft()
            offset[d].append(cur.val)
            if cur.left:
                q.append((cur.left, d - 1))
            if cur.right:
                q.append((cur.right, d + 1))
        return [offset[d] for d in sorted(offset.keys())]