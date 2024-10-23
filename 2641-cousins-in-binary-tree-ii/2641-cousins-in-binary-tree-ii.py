# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum = self.getLevelSum(root)
        # for each parent:
        # newLeftChildVal = newRightChildVal = levelSum - (oldLeftChildVal + oldRightChildVal)
        if root: root.val = 0
        q = deque([root])
        levelSum = self.getLevelSum(root)
        level = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                childrenSum = (cur.left.val if cur.left else 0) + (cur.right.val if cur.right else 0)
                if cur.left:
                    cur.left.val = levelSum[level] - childrenSum
                    q.append(cur.left)
                if cur.right:
                    cur.right.val = levelSum[level] - childrenSum
                    q.append(cur.right)
            level += 1
        return root
    
    def getLevelSum(self, root):
        dic = {}
        q = deque([root])
        levelSum = []
        while q:
            curSum = 0
            for _ in range(len(q)):
                cur = q.popleft()
                curSum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            levelSum.append(curSum)     
        return levelSum