def find_min_arrow_shots(points):
    points.sort()
    ans = len(points)
    prev = points[0]

    for i in range(1, len(points)):
        if points[i][0] <= prev[1]:
            ans -= 1
            prev = [points[i][0], min(points[i][1], prev[1])]
        else:
            prev = points[i]

    return ans
