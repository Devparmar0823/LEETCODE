import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            total_time = sum(math.ceil(p / k) for p in piles)
            
            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
