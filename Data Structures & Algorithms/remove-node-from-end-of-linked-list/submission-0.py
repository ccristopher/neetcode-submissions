# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # end of list, n - 1 spaces to the left 
        dummy = tail = ListNode()
        tail.next = head
        for _ in range(n - 1):
            head = head.next

        while head.next:
            head = head.next
            tail = tail.next
        
        tail.next = tail.next.next

        return dummy.next