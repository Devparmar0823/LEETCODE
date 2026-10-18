from typing import List


class UnionFind:

  def __init__(self):
    self.parent = {}
    self.count = 0  # Tracks number of unique connected components

  def find(self, i: int) -> int:
    if i not in self.parent:
      self.parent[i] = i
      self.count += 1
    if self.parent[i] == i:
      return i
    # Path compression
    self.parent[i] = self.find(self.parent[i])
    return self.parent[i]

  def union(self, i: int, j: int):
    root_i = self.find(i)
    root_j = self.find(j)
    if root_i != root_j:
      self.parent[root_i] = root_j
      self.count -= 1  # Successfully merged two components


class Solution:

  def removeStones(self, stones: List[List[int]]) -> int:
    uf = UnionFind()

    for r, c in stones:
      # Use bitwise NOT (~c) or c + 10001 to ensure row and column identifiers do not collide
      uf.union(r, ~c)

    # Max stones removed = Total stones - Number of remaining components
    return len(stones) - uf.count
