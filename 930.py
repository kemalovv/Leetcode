def num_subarrays_with_sum(nums, goal):
    def count(x):
        if x < 0:
            return 0
        ans, cur, left = 0, 0, 0

        for right in range(len(nums)):
            cur += nums[right]
            while cur > x:
                cur -= nums[left]
                left += 1
            ans += right - left + 1

        return ans

    return count(goal) - count(goal - 1)
