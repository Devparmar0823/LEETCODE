from collections import deque
from typing import List


class Solution:

  def isBipartite(self, graph: List[List[int]]) -> bool:
    n = len(graph)
    # 0 means uncolored, 1 means Color A, -1 means Color B
    color = [0] * n

    # Loop through all nodes because the graph might be disconnected
    for i in range(n):
      if color[i] != 0:
        continue

      # Start BFS for the uncolored component
      queue = deque([i])
      color[i] = 1  # Start with Color A (1)

      while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
          # If the neighbor has the same color, a conflict is found
          if color[neighbor] == color[node]:
            return False

          # If the neighbor is uncolored, color it with the opposite color
          if color[neighbor] == 0:
            color[neighbor] = -color[node]  # Flips 1 to -1 or -1 to 1
            queue.append(neighbor)

    return True
