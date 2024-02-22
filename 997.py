from collections import defaultdict


def find_judge(n, trust):
    if n == 1:
        return 1

    whom_trust = defaultdict(list)
    who_trust = defaultdict(list)

    for i in trust:
        whom_trust[i[1]].append(i[0])
        who_trust[i[0]].append([[1]])

    for k, v in whom_trust.items():
        if len(v) == n - 1 and k not in who_trust.keys():
            return k

    return -1
