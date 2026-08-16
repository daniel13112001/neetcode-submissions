# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        listSum = ListNode()
        cur = listSum
        carry = 0
        
        while l1 and l2:
            curSum = l1.val + l2.val + carry
            if curSum >= 10:
                rem = curSum - 10
                carry = 1
            else:
                rem = curSum
                carry = 0
            cur.next = ListNode(rem)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        rest = None
        if l1:
            rest = l1
        if l2:
            rest = l2
        
        while rest:
            curSum = rest.val + carry
            if curSum >= 10:
                rem = curSum - 10
                carry = 1
            else:
                rem = curSum
                carry = 0
            cur.next = ListNode(rem)
            cur = cur.next
            rest = rest.next


        if carry > 0:
            cur.next = ListNode(carry)



        return listSum.next



        