def middle_node(head):
    ans, length = head, head
    ans_i = 0

    while length.next:
        length = length.next
        ans_i += 1

    if not ans_i % 2:
        ans_i //= 2
    else:
        ans_i //= 2
        ans_i += 1

    while ans_i:
        ans = ans.next
        ans_i -= 1

    return ans
