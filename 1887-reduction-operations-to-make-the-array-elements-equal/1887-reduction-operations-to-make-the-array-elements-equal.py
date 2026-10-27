class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        cur_step=0
        total_step=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cur_step+=1
            total_step+=cur_step
        return total_step