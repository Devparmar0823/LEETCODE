class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        maxXor = 0
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        for num in nums:
            node = root
            currentXor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggledBit = 1 - bit
                if toggledBit in node:
                    currentXor |= (1 << i)
                    node = node[toggledBit]
                else:
                    node = node[bit]
                    
            maxXor = max(maxXor, currentXor)
            
        return maxXor
