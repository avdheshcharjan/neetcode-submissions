# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#simple solution but can use RECURSION AS WELL
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1
        
        newNode=ListNode()
        curr= newNode

        while list1 and list2:
            if list1.val<= list2.val:
                newNode.next=list1
                list1=list1.next
            else:
                newNode.next=list2
                list2=list2.next
            
            newNode=newNode.next

        #below lines could also be written as:
        #newNode.next = list1 or list2
        if list1:
            newNode.next=list1

        if list2:
            newNode.next=list2


        return curr.next