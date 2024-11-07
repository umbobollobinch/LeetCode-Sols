# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def register(node, n, i = 0):
    if node.next is None:
        i += 1
    else:
        node.next, i = register(node.next, n, i)
        i += 1

    if i == n:
        node = node.next

    return (node, i)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        nl, _ = register(head, n)
        return(nl)
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
