# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def digger(root, list):
    if root is None:
        return root            
    elif root.left is None:
        list.append(root.val)
    else:
        digger(root.left, list)
        list.append(root.val)
            
    if root.right is None:
        return list
    else:
        digger(root.right, list)    
        
    return list
    
    
class Solution(object):
    def inorderTraversal(self, root, list = []):
        list = []
        return digger(root, list)
        
    
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
