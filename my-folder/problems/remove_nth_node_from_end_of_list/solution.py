# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        temp = head
        count = 1
        while(temp and temp.next):
            temp = temp.next
            count+=1
        if((count-n)==0):
            head = head.next
            return head
        temp = head
        indx=1
        while(temp and temp.next and indx!=(count-n)):
            indx+=1
            temp = temp.next
        if temp.next and temp.next.next:
            temp.next = temp.next.next
        else: temp.next = None
        return head