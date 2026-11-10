class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less=[]
        great=[]
        eq=[]
        for num in nums:
            if num<pivot:
                less.append(num)
            elif num==pivot:
                eq.append(num)
            else:
                great.append(num)
        nums=less+eq+great
        return nums