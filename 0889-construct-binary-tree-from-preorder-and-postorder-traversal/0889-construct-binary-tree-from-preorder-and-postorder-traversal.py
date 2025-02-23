# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder[0])
        if len(preorder) > 1:
            leftRootVal = preorder[1] #note that if a tree with only right child will have the same pre + postorder traversal as one with only left child. So we can generalize by choosing preoder[1] as left child
            l = postorder.index(leftRootVal)
            if l == len(preorder) - 2: #no right child
                root.left = self.constructFromPrePost(preorder[1:], postorder[:-1])
            else:
                rightRootVal = postorder[-2]
                r = preorder.index(rightRootVal)                
                root.left = self.constructFromPrePost(preorder[1:r], postorder[:l+1])
                root.right = self.constructFromPrePost(preorder[r:], postorder[l+1:-1])
        return root
        #We can build a dic instead of using .index() to reduce time complexity from O(n^2) to O(n) but this code is easier to understand