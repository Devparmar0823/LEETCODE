class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        max_xor = 0
        mask = 0
        
        # Consider a 32-bit integer. Standard constraint is usually up to 10^5, 
        # so 31 bits (0 to 30) are sufficient for non-negative integers.
        for i in range(30, -1, -1):
            # The mask helps us isolate the prefixes of the numbers up to bit i
            mask |= (1 << i)
            
            # Extract the prefixes of all numbers down to the i-th bit
            prefixes = {num & mask for num in nums}
            
            # Greedy choice: Can we achieve a '1' at the i-th bit position?
            candidate = max_xor | (1 << i)
            
            # XOR property: If A ^ B = C, then A ^ C = B.
            # If 'candidate ^ pref' exists in our set, then 'candidate' is achievable.
            for pref in prefixes:
                if (candidate ^ pref) in prefixes:
                    max_xor = candidate
                    break
                    
        return max_xor
