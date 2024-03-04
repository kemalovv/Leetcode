def bag_of_tokens_score(tokens, power):
    tokens.sort()
    left = 0
    right = len(tokens) - 1
    ans = 0

    if tokens[0] > power or not tokens:
        return ans

    while left != right:
        if tokens[left] <= power:
            power -= tokens[left]
            ans += 1
            left += 1
        else:
            power += tokens[right]
            ans -= 1
            right -= 1

    if tokens[left] <= power:
        return ans + 1
    else:
        return ans
