# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # curr=head
        # prev=None
        fast, slow=head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # curr=slow
        
        curr=slow.next
        slow.next = None
        prev = None

        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next

    # prev is the head of the second half reversed LL
        # while head:
        #     next=head.next
        #     head.next=prev
        #     prev.next=next
        first, last= head, prev
        while last:
            tf, tl= first.next, last.next
            first.next=last
            last.next=tf
            first, last = tf,tl
