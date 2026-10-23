class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        output=[]
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even[0]
                even.remove(even[0])
            else:
                nums[i]=odd[0]
                odd.remove(odd[0])
        return nums