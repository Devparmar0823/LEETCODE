class Solution:
    def isFascinating(self, n: int) -> bool:
        result=str(n)+str(2*n)+str(3*n)
        return "".join(sorted(result))=="123456789"