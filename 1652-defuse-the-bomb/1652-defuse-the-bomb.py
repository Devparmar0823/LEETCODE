class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        length=len(code)
        output=[0]*length
        if k==0:
            return output
        i=0
        while i<length:
            total=0
            if k>0:
                n=1
                while n<=k:
                    total+=code[(i+n)%length]
                    n+=1
            else:
                n=1
                while n<=abs(k):
                    total+=code[(i-n)%length]
                    n+=1
            output[i]=total
            i+=1
        return output