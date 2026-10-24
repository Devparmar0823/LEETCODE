class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort()
        seen=set()
        left=0
        right=len(nums)-1
        while left<right:
            avg=(nums[left]+nums[right])/2
            if avg not in seen:
                seen.add(avg)
            left+=1
            right-=1
        return len(seen)