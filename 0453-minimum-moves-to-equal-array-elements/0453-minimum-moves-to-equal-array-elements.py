class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        move = 0
        for i in range(1, len(nums)):
            move += nums[i] - nums[0]
        return move