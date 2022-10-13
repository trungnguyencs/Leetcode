"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, nAryRoot: 'Optional[Node]') -> Optional[TreeNode]:
        if not nAryRoot: return None
        binaryRoot = TreeNode(nAryRoot.val)
        for i, child in enumerate(nAryRoot.children): # left is neighbor, right is child
            if i == 0:
                cur = binaryRoot.right = self.encode(child)
            else:
                cur.left = self.encode(child)
                cur = cur.left
        return binaryRoot
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, binaryRoot: Optional[TreeNode]) -> 'Optional[Node]':
        if not binaryRoot: return None
        root = Node(binaryRoot.val, children=[])
        child = binaryRoot.right
        while child:
            root.children.append(self.decode(child))
            child = child.left
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))