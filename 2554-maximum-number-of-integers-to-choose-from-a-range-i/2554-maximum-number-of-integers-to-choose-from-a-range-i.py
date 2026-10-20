class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        seen=set(banned)
        cur_sum=0
        count=0
        for i in range(1,n+1):
            if i in seen:
                continue
            if cur_sum+i>maxSum:
                break
            cur_sum+=i
            count+=1
        return count