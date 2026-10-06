class Solution:
    def arrangeCoins(self, n: int) -> int:
        comp_rows=0
        i=1
        while n>0 and i<n+1:
            comp_rows+=1
            n-=i
            i+=1
        return comp_rows