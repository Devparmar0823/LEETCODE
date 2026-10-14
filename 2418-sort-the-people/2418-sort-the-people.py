class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(heights)
        
        # Repeat until you place the correct person at every index i
        for i in range(n):
            # 1. Assume the current position has the tallest person
            tallest_idx = i
            
            # 2. Find the actual tallest person in the remaining unsorted part
            for j in range(i + 1, n):
                if heights[j] > heights[tallest_idx]:
                    tallest_idx = j
            
            # 3. Swap both the heights and names to keep them in sync
            heights[i], heights[tallest_idx] = heights[tallest_idx], heights[i]
            names[i], names[tallest_idx] = names[tallest_idx], names[i]
            
        return names
