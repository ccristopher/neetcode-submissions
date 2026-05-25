# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            res = list1
            curr = list1
            list2Next = list2
            list1Next = list1.next
        else:
            res = list2
            curr = list2
            list1Next = list1
            list2Next = list2.next

        while list1Next and list2Next:
            if list1Next.val < list2Next.val:
                print("case one")
                print(list1Next.val)
                print(list2Next.val)
                temp = list1Next.next
                curr.next = list1Next
                curr = curr.next
                list1Next = temp
            else:
                print("case two")
                print(list1Next.val)
                print(list2Next.val)
                temp = list2Next.next
                curr.next = list2Next
                curr = curr.next
                list2Next = temp
        
        if list1Next:
            curr.next = list1Next
        elif list2Next:
            curr.next = list2Next

        return res