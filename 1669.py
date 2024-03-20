def merge_in_between(list1, a, b, list2):
    ans = ListNode(0, list1)
    dummy = ans.next
    index = 0

    while index < a - 1:
        dummy = dummy.next
        list1 = list1.next
        index += 1

    while index < b + 1:
        index += 1
        list1 = list1.next

    dummy.next = list2

    while dummy.next:
        dummy = dummy.next

    dummy.next = list1
    return ans.next
