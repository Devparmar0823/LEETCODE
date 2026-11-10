class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            left_sum=0
            right_sum=0
            if i==0:
                left_sum=0
            if i==len(nums)-1:
                right_sum=0
            for j in range(i):
                left_sum+=nums[j]
            for k in range(i+1,len(nums)):
                right_sum+=nums[k]
            answer.append(abs(left_sum-right_sum))
        return answer