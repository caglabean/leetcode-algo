# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class List:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def print_list(self):
        curr_node = self.head  # Make a copy of head node to avoid changing the actual head
        print("Printing the linked list:")
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next
        # a - b - c - none
        # none <- a <- b <- c
        # prev   curr next
        #        prev curr
        #             prev curr
        #                  prev
        # c - b - a - none

    def reverseList(self, head):
        previous_node = None
        curr_node = head
        next_node = curr_node
        while next_node:
            next_node = curr_node.next
            curr_node.next = previous_node
            previous_node = curr_node
            if next_node:
                curr_node = next_node

        return curr_node


ll = List()
ll.append(12)
ll.append(13)
ll.append(14)
ll.print_list()
ll.head = ll.reverseList(ll.head)
ll.print_list()
