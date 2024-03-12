import collections


def remove_zero_sum_sublists(head):
    curr = dummy = ListNode(0)
    dummy.next = head
    prefix = 0
    seen = collections.OrderedDict()

    while curr:
        prefix += curr.val

        if prefix not in seen:
            seen[prefix] = curr
        else:
            node = seen[prefix]
            node.next = curr.next
            while list(seen.keys())[-1] != prefix:
                seen.popitem()

        curr = curr.next

    return dummy.next
