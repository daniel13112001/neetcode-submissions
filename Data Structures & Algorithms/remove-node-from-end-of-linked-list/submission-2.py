# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummyHead = ListNode()
        dummyHead.next = head


        slow = dummyHead
        fast = dummyHead

        for i in range(n): 
            if fast and fast.next:
                fast = fast.next


        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        removed = slow.next
        slow.next = slow.next.next
        removed.next = None


        return dummyHead.next

        