from typing import List


class Solution:

  def largestIsland(self, grid: List[List[int]]) -> int:
    n = len(grid)
    island_sizes = {}
    next_id = 2
    max_area = 0

    # 1. Helper function to explore and label an island using DFS
    def get_island_size(r: int, c: int, island_id: int) -> int:
      if not (0 <= r < n and 0 <= c < n) or grid[r][c] != 1:
        return 0
      grid[r][c] = island_id  # Label cell with unique ID
      size = 1
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        size += get_island_size(r + dr, c + dc, island_id)
      return size

    # Pass 1: Find all islands, label them, and store their sizes
    for r in range(n):
      for c in range(n):
        if grid[r][c] == 1:
          size = get_island_size(r, c, next_id)
          island_sizes[next_id] = size
          max_area = max(max_area, size)
          next_id += 1

    # Pass 2: Evaluate every '0' cell to see what islands it can connect
    for r in range(n):
      for c in range(n):
        if grid[r][c] == 0:
          # Use a set to avoid counting the same island multiple times
          neighbor_islands = set()

          for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
              neighbor_islands.add(grid[nr][nc])

          # Potential size is 1 (the flipped cell) + sum of distinct neighbors
          possible_size = 1 + sum(
              island_sizes[i_id] for i_id in neighbor_islands
          )
          max_area = max(max_area, possible_size)

    return max_area
