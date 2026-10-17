class TrieNode:
    def __init__(self):
        self.children = {} # Maps bit 0 or 1 to the next TrieNode

class Solution:
    def maximizeXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        # 1. Sort the input numbers in ascending order
        nums.sort()
        
        # 2. Store the original query index so we can place answers in the correct positions
        # Each element becomes: (m_i, x_i, original_index)
        sorted_queries = sorted([(q[1], q[0], i) for i, q in enumerate(queries)])
        
        result = [-1] * len(queries)
        root = TrieNode()
        num_idx = 0
        n = len(nums)
        
        # Helper function to insert a number bit-by-bit into the Trie
        def insert(num: int):
            node = root
            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
                
        # Helper function to find the maximum XOR for value x
        def query_trie(x: int) -> int:
            if not root.children: # Trie is empty
                return -1
            
            node = root
            max_xor = 0
            for i in range(30, -1, -1):
                bit = (x >> i) & 1
                toggled_bit = 1 - bit
                
                # If the opposite bit is available, we take it to maximize XOR
                if toggled_bit in node.children:
                    max_xor |= (1 << i)
                    node = node.children[toggled_bit]
                else:
                    node = node.children[bit]
            return max_xor

        # 3. Process sorted queries sequentially
        for m, x, original_idx in sorted_queries:
            # Insert all elements from nums that are less than or equal to current m
            while num_idx < n and nums[num_idx] <= m:
                insert(nums[num_idx])
                num_idx += 1
                
            # Query the Trie for the current x value
            result[original_idx] = query_trie(x)
            
        return result
