# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.dfs(root, 0)

    #instead of using a hashset, this solution finds the path from root for each number
    #notice that level-by-level of the tree will be in the form [[0], [1, 2], [3, 4, 5, 6]]
    #if we aff 1 to all nums it will be [[1], [2, 3], [4, 5, 6, 7]]
    #in binary will be [[1], [10, 11], [100, 101, 110, 111]]
    #so 0 means turn left, 1 means turn right
    def find(self, target: int) -> bool:
        cur = self.root
        bits = bin(target + 1)[3:] #trim '0b1'
        for b in bits:
            if b == '0':
                if not cur.left: return False
                cur = cur.left
            elif b == '1':
                if not cur.right: return False
                cur = cur.right
        return True

    def dfs(self, root, val):
        root.val = val
        if root.left:
            self.dfs(root.left, 2 * val + 1)
        if root.right:
            self.dfs(root.right, 2 * val + 2)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)