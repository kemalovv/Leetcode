def rearrange_array(nums):
    ans = []
    negative = []

    for i in nums:
        if i > 0:
            ans.append(i)
            ans.append(0)
        else:
            negative.append(i)

    index = 1

    for j in negative:
        ans[index] = j
        index += 2

    return ans
