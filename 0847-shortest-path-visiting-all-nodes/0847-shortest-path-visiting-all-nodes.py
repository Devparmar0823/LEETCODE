from collections import deque


class Solution:

  def shortestPathLength(self, graph: list[list[int]]) -> int:
    n = len(graph)
    # The mask when all nodes have been visited (e.g., for 3 nodes: 111 in binary = 7)
    all_visited = (1 << n) - 1

    # Queue stores: (current_node, visited_nodes_bitmask, current_path_length)
    queue = deque()

    # Set to track visited states to avoid redundant work: (current_node, visited_nodes_bitmask)
    visited_states = set()

    # Since we can start at any node, add all nodes to the queue initially
    for i in range(n):
      initial_mask = 1 << i
      queue.append((i, initial_mask, 0))
      visited_states.add((i, initial_mask))

    # BFS traversal
    while queue:
      node, mask, steps = queue.popleft()

      # If all nodes have been visited, return the steps taken
      if mask == all_visited:
        return steps

      # Explore neighbors
      for neighbor in graph[node]:
        next_mask = mask | (1 << neighbor)

        # Only visit this state if it hasn't been explored before
        if (neighbor, next_mask) not in visited_states:
          visited_states.add((neighbor, next_mask))
          queue.append((neighbor, next_mask, steps + 1))

    return 0
