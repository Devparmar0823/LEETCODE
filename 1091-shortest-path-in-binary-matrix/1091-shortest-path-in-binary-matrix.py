from collections import deque
from typing import List


class Solution:

  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    n = len(grid)

    # 1. Base case: If the start or end cell is blocked, no path exists
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
      return -1

    # 2. Define all 8 possible directions (horizontal, vertical, diagonal)
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    # 3. Initialize BFS queue: (row, col, path_length)
    queue = deque([(0, 0, 1)])

    # 4. Mark the starting cell as visited (mutating in-place to save space)
    grid[0][0] = 1

    while queue:
      r, c, dist = queue.popleft()

      # If we reached the destination, return the distance
      if r == n - 1 and c == n - 1:
        return dist

      # Explore all 8 neighbors
      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        # Check boundaries and if the neighbor cell is unvisited (0)
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
          grid[nr][nc] = 1  # Mark as visited right away to avoid duplicate queues
          queue.append((nr, nc, dist + 1))

    return -1
