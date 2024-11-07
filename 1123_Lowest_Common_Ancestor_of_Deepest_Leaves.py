# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def digger(root):
        a = 1 if root.left is None else 1 + digger(root.left)
        b = 1 if root.right is None else 1 + digger(root.right)
        return max([a,b])

class Solution(object):        
    def lcaDeepestLeaves(self, root):
        a = 0 if root.left is None else digger(root.left)
        b = 0 if root.right is None else digger(root.right)
        # print(a,b)
        
        if a > b:
            return self.lcaDeepestLeaves(root.left)
        elif a < b:
            return self.lcaDeepestLeaves(root.right)
        else:
            return root
        
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
