# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       if not head:
           return None
       curr, ret = head, head.next
       while ret and ret.next:
           curr = curr.next
           ret = ret.next.next
       temp = curr.next
       curr.next = None
       prev = None
       while(temp):
            ret = temp.next
            temp.next = prev
            prev = temp
            temp = ret
       curr = head
       while prev:
            second = prev.next
            temp2 = curr.next
            prev.next = temp2
            curr.next = prev
            prev = second
            curr = temp2
       return head
            


       