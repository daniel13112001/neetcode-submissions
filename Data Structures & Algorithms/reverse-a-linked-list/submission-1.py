# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        prevNode = None
        curNode = head
        nextNode = head.next

        while nextNode != None:
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            nextNode = curNode.next
        curNode.next = prevNode
        return curNode
        