# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # my approach was to first reverse then remove from 'prev' then reverse again but kinda lengthy
        
        # prev=None
        # curr=head
        # while curr is not None:
        #     next=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=next
        length=0
        curr=head
        while curr.next:
            length+=1
            curr=curr.next
        # return curr will return the length of LL
        # return curr
        index=length-n+1
        if index==0:
            return head.next #edge case of removing head
        # temp=head
        # prev=None
        # while temp:
        #     next=temp.next
        #     if temp==index:
        curr=head
        # WE CAN TRAVERSE TO (index - 1)
        for i in range(index-1):
            curr=curr.next
        
        #then link it to .next.next
        curr.next=curr.next.next

        return head
        
        




        



