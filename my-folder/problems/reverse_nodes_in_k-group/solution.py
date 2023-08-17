# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        while True:
            m = self.kth(tail, k)
            if not m:
                break
            d = m.next
            prev = m.next
            temp2 = tail.next
            while(temp2!=d):
                nxt = temp2.next
                temp2.next = prev
                prev = temp2
                temp2 = nxt
            temp = tail.next
            tail.next = m
            tail = temp

        return dummy.next
    def kth(self, head, k):
        cur = head
        while cur and k>0:
            k-=1
            cur = cur.next
        return cur