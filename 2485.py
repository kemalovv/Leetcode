def pivot_integer(n):
    current_sum = 0
    nums = range(1, n + 1)
    total = sum(nums)

    for num in nums:
        current_sum += num

        if current_sum == total:
            return num

        total -= num

    return -1
