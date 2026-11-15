class Solution:
    def countTestedDevices(self, bp: List[int]) -> int:
        count=0
        for i in range(len(bp)):
            if bp[i]>0:
                count+=1
                for j in range(i+1,len(bp)):
                    bp[j]=max(0,bp[j]-1)
            else:
                continue
        return count