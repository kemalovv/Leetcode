def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

    # O(n)
    # n = len(nums)
    #
    #     for i in range(n + 1):
    #         if i not in nums:
    #             return i
