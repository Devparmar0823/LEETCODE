import heapq
from typing import List


class Solution:

  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    rows, cols = len(heights), len(heights[0])

    # 1. Initialize a 2D array to store the minimum effort to reach each cell
    # Start with infinity for all cells except the top-left cell
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0

    # 2. Priority Queue stores tuples of (current_effort, row, col)
    min_heap = [(0, 0, 0)]

    # 4-directional moves (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while min_heap:
      current_effort, r, c = heapq.heappop(min_heap)

      # If we reached the bottom-right corner, we can return early
      if r == rows - 1 and c == cols - 1:
        return current_effort

      # If we found a path with a larger effort than already recorded, skip it
      if current_effort > efforts[r][c]:
        continue

      # Explore neighbors
      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
          # The effort for this transition is the max absolute difference
          new_effort = max(
              current_effort, abs(heights[r][c] - heights[nr][nc])
          )

          # If this new path yields a lower effort to reach (nr, nc), update it
          if new_effort < efforts[nr][nc]:
            efforts[nr][nc] = new_effort
            heapq.heappush(min_heap, (new_effort, nr, nc))

    return 0
