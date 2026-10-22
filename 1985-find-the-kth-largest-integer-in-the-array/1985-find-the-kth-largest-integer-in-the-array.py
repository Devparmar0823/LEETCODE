class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        return str(nums[-k])