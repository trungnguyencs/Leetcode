# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        if not root.left and not root.right: return [root.val]
        lBoundary, mBoundary, rBoundary = self.getLeftBoundary(root.left), self.getMiddleBoundary(root), self.getRightBoundary(root.right)
        return [root.val] + lBoundary + mBoundary + rBoundary
        
    def getMiddleBoundary(self, root):
        mBoundary = []
        def preOrder(root):
            if not root.left and not root.right: mBoundary.append(root.val)
            if root.left: preOrder(root.left)
            if root.right: preOrder(root.right)
        preOrder(root)
        return mBoundary
        
    def getLeftBoundary(self, root):
        if not root: return []
        lBoundary = []
        while root:
            lBoundary.append(root.val)
            root = root.left if root.left else root.right
        return lBoundary[:-1] #exclude last leaf
    
    def getRightBoundary(self, root):
        if not root: return []
        rBoundary = []
        while root:
            rBoundary.append(root.val)
            root = root.right if root.right else root.left
        return rBoundary[:-1][::-1] #exclude last leaf