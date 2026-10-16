class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        output=[]
        i=0
        while k>0 and i<len(nums):
            if nums[i] in output:
                i+=1
                continue
            else:
                output.append(nums[i])
                i+=1
                k-=1
        return output    