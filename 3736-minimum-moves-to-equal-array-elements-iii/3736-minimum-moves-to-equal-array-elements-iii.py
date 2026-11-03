class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=max(nums)
        moves=0
        for num in nums:
            moves+=n-num
        return moves