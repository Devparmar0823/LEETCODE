class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=[]
        neg=[]
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        result=[]
        for i in range(len(nums)//2):
            result.extend([pos[i],neg[i]])
        return result