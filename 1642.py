import heapq


def furthest_building(heights, bricks, ladders):
    used_bricks = []

    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue

        bricks -= diff
        heapq.heappush(used_bricks, -diff)

        if bricks < 0:
            if not ladders:
                return i
            ladders -= 1
            bricks += -heapq.heappop(used_bricks)

    return len(heights) - 1
