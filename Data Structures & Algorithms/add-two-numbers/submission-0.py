# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr1 = l1
        curr2 = l2
        carry = 0
        curr = dummy

        while curr1 or curr2 or carry:
            dig1 = curr1.val if curr1 else 0
            dig2 = curr2.val if curr2 else 0

            total = dig1 + dig2 +carry


            carry = total//10
            digit = total%10

            newn = ListNode(digit)
            curr.next = newn


            if curr1:
                curr1 = curr1.next
            if curr2 :
                curr2 = curr2.next
            if curr:
                curr = curr.next
        return dummy.next
            
            