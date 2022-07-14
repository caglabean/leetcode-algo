# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        curr = None
        if list1 and list2:
            if list1.val <= list2.val:
                curr = list1
                list1 = curr.next
            else:
                curr = list2
                list = curr.next
            new_head = curr
        else:
            return list1 if list1 else list2

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        if list1 is None:
            curr.next = list2
        else:
            curr.next = list1
        return new_head
