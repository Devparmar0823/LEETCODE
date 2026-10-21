class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        while nums:
            n=max(nums)
            if -n in nums:
                return n
            else:
                nums.remove(n)
        return -1