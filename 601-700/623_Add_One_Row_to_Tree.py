# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dig(node, val, tgt, depth = 1):
    if depth == tgt - 1:
        node.left = TreeNode(val = val, left = node.left)
        node.right = TreeNode(val = val, right = node.right)
    else:
        if node.left is not None:
            
            dig(node.left, val, tgt, depth + 1)
        if node.right is not None:
            dig(node.right, val, tgt, depth + 1)

class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth == 1 :
            return TreeNode(val = val, left = root)
        else:
            dig(root, val, depth)
            return root
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        
