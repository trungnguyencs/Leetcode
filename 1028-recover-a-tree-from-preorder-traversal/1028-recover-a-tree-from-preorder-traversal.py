# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack, i = [], 0
        while i < len(traversal):
            level = val = 0
            while i < len(traversal) and traversal[i] == '-':
                level, i = level + 1, i + 1
            while i < len(traversal) and traversal[i] != '-':
                val, i = val * 10 + int(traversal[i]), i + 1
            #If the size of stack is bigger than the level of node, we pop the stack until it's not
            while len(stack) > level: 
                stack.pop()
            node = TreeNode(val)
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]