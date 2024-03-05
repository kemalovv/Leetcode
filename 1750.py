def minimum_length(s):
    if len(s) == 1:
        return 1

    left = 0
    right = len(s) - 1

    while s[left] == s[right]:
        while left + 1 <= right and s[left + 1] == s[left]:
            left += 1

        while right - 1 >= left and s[right - 1] == s[right]:
            right -= 1

        if left != right and left + 1 != right:
            left += 1
            right -= 1
        else:
            break

    if left == right and s[left - 1] == s[right]:
        return 0
    elif left == right and s[left - 1] != s[right]:
        return 1
    else:
        return right - left + 1
