# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode()
        cur = dummyHead

        list1Cur = list1
        list2Cur = list2

        while list1Cur and list2Cur:

            while list1Cur and list2Cur and list1Cur.val  <= list2Cur.val :
                cur.next = list1Cur
                list1Cur = list1Cur.next
                cur = cur.next
            

            while list1Cur and list2Cur and list2Cur.val  <= list1Cur.val :
                cur.next = list2Cur
                list2Cur = list2Cur.next
                cur = cur.next

        # In case one list is exhausted and there's still stuff left in the second list
        while list1Cur:
            cur.next = list1Cur
            list1Cur = list1Cur.next
            cur = cur.next
        
        while list2Cur:
            cur.next = list2Cur
            list2Cur = list2Cur.next
            cur = cur.next


        return dummyHead.next
        