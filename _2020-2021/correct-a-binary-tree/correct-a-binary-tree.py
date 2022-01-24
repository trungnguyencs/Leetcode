# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = deque([(root, None)])
        while q:
            levelVisited = set()
            for _ in range(len(q)):
                cur, parent = q.popleft()
                if cur.right in levelVisited:
                    if parent.left is cur:
                        parent.left = None
                    else:
                        parent.right = None
                    break
                levelVisited.add(cur)
                if cur.right:
                    q.append((cur.right, cur))
                if cur.left:
                    q.append((cur.left, cur))
        return root
                
                    
