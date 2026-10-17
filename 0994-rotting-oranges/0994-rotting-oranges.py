from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes_elapsed = 0
        
        # Step 1: Initialize the queue with all initially rotten oranges
        # and count the total number of fresh oranges.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
                    
        # If there are no fresh oranges to begin with, 0 minutes are needed.
        if fresh_oranges == 0:
            return 0
            
        # Step 2: Multi-source BFS tracking layers (minutes)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
        
        while queue and fresh_oranges > 0:
            minutes_elapsed += 1
            
            # Process all currently rotten oranges for this minute frame
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check grid boundaries and see if neighbor is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2       # Contaminate it
                        fresh_oranges -= 1     # Decrement fresh count
                        queue.append((nr, nc)) # Enqueue for next minute
                        
        # Step 3: If fresh oranges still remain, it's impossible to rot all of them
        return minutes_elapsed if fresh_oranges == 0 else -1
