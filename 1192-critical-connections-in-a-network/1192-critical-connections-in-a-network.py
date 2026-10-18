from collections import defaultdict
from typing import List


class Solution:

  def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
    graph = defaultdict(list)
    for u, v in connections:
      graph[u].append(v)
      graph[v].append(u)

    # rank[i] stores the discovery time of node i
    rank = [-1] * n
    critical_edges = []

    def dfs(node: int, parent: int, current_rank: int) -> int:
      rank[node] = current_rank
      min_rank = current_rank

      for neighbor in graph[node]:
        if neighbor == parent:
          continue

        # FIX: If neighbor is already visited, it's a back-edge. 
        # Directly update min_rank with the neighbor's discovery rank without recursing.
        if rank[neighbor] != -1:
          min_rank = min(min_rank, rank[neighbor])
        else:
          # If not visited, perform DFS on the neighbor
          neighbor_rank = dfs(neighbor, node, current_rank + 1)

          # If neighbor's lowest reachable rank is strictly greater than current_rank,
          # it cannot bypass this node to reach an ancestor, making it a bridge.
          if neighbor_rank > current_rank:
            critical_edges.append([node, neighbor])

          min_rank = min(min_rank, neighbor_rank)

      return min_rank

    dfs(0, -1, 0)
    return critical_edges
