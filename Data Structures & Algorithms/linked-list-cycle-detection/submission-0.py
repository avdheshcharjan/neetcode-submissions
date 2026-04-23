# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow, fast = head, head
        # while slow and slow.next:
        #     if fast and fast.next:
        #         slow=slow.next
        #         fast=fast.next.next

        # else:
        #     return False
        slow, fast = head, head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        # can we also compare the values of the LL.val because of a sorted LL??? 
        # so if fast.val > slow.val then a cycle detected
        
        