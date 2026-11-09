class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_streak = -1
        for num in nums:
            curr = num
            streak = 0
            while curr in num_set:
                streak += 1
                curr = curr ** 2
            if streak >= 2:
                max_streak = max(max_streak, streak)
        return max_streak