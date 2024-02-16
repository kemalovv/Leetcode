from collections import Counter


def find_least_num_of_unique_ints(arr, k):
    nums_count = Counter(arr)
    values = sorted(nums_count.values())
    ans = 0

    for i in range(len(values)):
        if k - values[i] >= 0:
            k -= values[i]
        else:
            ans += len(values) - i
            break

    return ans
