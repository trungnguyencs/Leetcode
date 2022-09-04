# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        dic = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            levelDic = defaultdict(list)
            for _ in range(len(q)):
                node, offset = q.popleft()
                levelDic[offset].append(node.val)
                if node.left:
                    q.append((node.left, offset - 1))
                if node.right:
                    q.append((node.right, offset + 1))
            for offset, arr in levelDic.items():
                dic[offset].extend(sorted(arr))
        return [dic[offset] for offset in sorted(dic.keys())]