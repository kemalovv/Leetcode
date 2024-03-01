def maximum_odd_binary_number(s):
    qty = s.count("1")
    length = len(s)
    ans = ""

    for i in range(length - 1):
        if qty > 1:
            ans += "1"
            qty -= 1
        else:
            ans += "0"

    return ans + "1"
