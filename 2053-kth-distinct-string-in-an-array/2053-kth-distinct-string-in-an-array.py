class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq={}
        for s in arr:
            if s in freq:
                freq[s]+=1
            else:
                freq[s]=1
        for s in arr:
            if freq[s]==1:
                k-=1
                if k==0:
                    return s
        return ""