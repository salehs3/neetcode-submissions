# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        prev = dummy
        for i in range(n):
            curr = curr.next

        while(curr.next != None):
            prev = prev.next
            curr = curr.next

        
        nexto = prev.next.next
        prev.next = nexto
       
        return dummy.next



        