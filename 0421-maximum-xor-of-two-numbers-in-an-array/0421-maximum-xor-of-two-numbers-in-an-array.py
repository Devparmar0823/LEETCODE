class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        maxXor = 0
        
        # Insert all numbers into the binary Trie
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
                
        # Find the maximum XOR for each number
        for num in nums:
            node = root
            currentXor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggledBit = 1 - bit
                
                # If the opposite bit exists, go that way to maximize XOR
                if toggledBit in node:
                    currentXor |= (1 << i)
                    node = node[toggledBit]
                else:
                    node = node[bit]
                    
            maxXor = max(maxXor, currentXor)
            
        return maxXor
