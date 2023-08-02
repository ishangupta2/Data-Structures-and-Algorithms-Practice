# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        remdr = 0
        dummy = ListNode()
        tail = dummy
        while(ptr1 and ptr2):
            val = ptr1.val + ptr2.val + remdr
            remdr = 0
            if val>=10:
                remdr = 1
                val = val % 10
            tail.next = ListNode(val)
            tail = tail.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        while ptr1:
            val = ptr1.val + remdr
            remdr = 0
            if val>=10:
                remdr = 1
                val = val % 10
            tail.next = ListNode(val)
            tail = tail.next
            ptr1 = ptr1.next
        while ptr2:
            val = ptr2.val + remdr
            remdr = 0
            if val>=10:
                remdr = 1
                val = val % 10
            tail.next = ListNode(val)
            tail = tail.next
            ptr2 = ptr2.next
        if remdr>0:
            tail.next = ListNode(1)
        return dummy.next
            