def first_missing_positive(nums):
    i = 0
    x = len(nums)

    while i < len(nums):
        if nums[i] <= 0:
            nums[i] = nums[-1]
            nums.pop()
            continue
        else:
            i += 1

    nums = set(nums)

    for j in range(1, x + 2):
        if j not in nums:
            return j
