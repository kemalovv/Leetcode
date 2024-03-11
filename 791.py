from collections import Counter


def custom_sort_string(order, s):
    s_count = Counter(s)
    ans = ""

    for i in order:
        if i in s_count:
            ans += i * s_count.pop(i)

    for k, v in s_count.items():
        ans += k * v

    return ans
