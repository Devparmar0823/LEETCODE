from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        for x in arr:
            remainder = ((x % k) + k) % k
            freq[remainder] += 1
        for i in range(k):
            if i == 0:
                if freq[0] % 2 != 0:
                    return False
            elif 2 * i == k:
                if freq[i] % 2 != 0:
                    return False
            else:
                if freq[i] != freq[k - i]:
                    return False 
        return True