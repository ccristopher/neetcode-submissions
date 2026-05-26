# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow = slow.next
        
        prev, curr, nextt = None, slow, slow.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev.next:
            temp = head.next
            head.next = prev
            temp2 = prev.next
            prev.next = temp

            head = temp
            prev = temp2