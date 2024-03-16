def find_max_length(nums):
    cache = {}
    zeros, ones = 0, 0
    ans = 0

    for i, v in enumerate(nums):
        if v == 0:
            zeros += 1
        else:
            ones += 1

        if ones - zeros not in cache:
            cache[ones - zeros] = i

        if ones == zeros:
            ans = ones + zeros
        else:
            ans = max(ans, i - cache[ones - zeros])

    return ans
