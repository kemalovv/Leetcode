def largest_perimeter(nums):
    nums.sort()
    prev_sum = nums[0] + nums[1]
    ans = 0

    if prev_sum > nums[2]:
        prev_sum += nums[2]
        ans += prev_sum
    else:
        prev_sum += nums[2]

    for i in range(3, len(nums)):
        if prev_sum > nums[i]:
            prev_sum += nums[i]
            ans = prev_sum
        else:
            prev_sum += nums[i]

    if ans:
        return ans
    else:
        return -1


print(largest_perimeter([5, 8, 34, 33, 6, 6, 42, 32, 29, 42]))
