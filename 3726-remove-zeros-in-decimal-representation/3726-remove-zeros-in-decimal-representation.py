class Solution:
    def removeZeros(self, n: int) -> int:
        nums=[]
        result=0
        while n>0:
            if n%10!=0:
                nums.append(n%10)
            n//=10
        nums.reverse()
        for num in nums:
            result=result*10+num
        return result