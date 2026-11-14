class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        score=[]
        for i in range(len(nums)):
            s=0
            if nums[i]%2==0:
                for j in range(i+1,len(nums)):
                    if nums[j]%2!=0:
                        s+=1
                score.append(s)
            else:
                for j in range(i+1,len(nums)):
                    if nums[j]%2==0:
                        s+=1
                score.append(s)
        return score 