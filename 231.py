def is_power_of_two(n):
    if n == 1 or n == 2:
        return True

    if n % 2:
        return False

    cur = 2
    while cur < n:
        cur *= 2

        if cur == n:
            return True

    return False
