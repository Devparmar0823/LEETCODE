class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        MAX_BIT = 30
        bit_count = [0] * MAX_BIT
        for num in nums:
            for i in range(MAX_BIT):
                if (num >> i) & 1:
                    bit_count[i] += 1
        ans = 0
        for _ in range(k):
            current_number = 0
            for i in range(MAX_BIT):
                if bit_count[i] > 0:
                    current_number |= (1 << i)
                    bit_count[i] -= 1  
            ans = (ans + current_number * current_number) % MOD
            
        return ans
