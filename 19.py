# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def remove_nth_from_end(head, n):
    first_node = ListNode(0, head)
    left_pointer = first_node
    right_pointer = head

    while n and right_pointer:
        right_pointer = right_pointer.next
        n -= 1

    while right_pointer:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    left_pointer.next = left_pointer.next.next

    return first_node.next
