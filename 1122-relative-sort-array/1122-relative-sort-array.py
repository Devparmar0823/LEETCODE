from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Map each element in arr2 to its index position for custom sorting priority
        pos = {num: i for i, num in enumerate(arr2)}
        
        # Sort using a tuple custom key:
        # 1. Elements in arr2 get their index position. Elements not in arr2 get a high priority index (len(arr2)) so they fall behind.
        # 2. Tiebreaker: Elements not in arr2 are sorted in ascending order by their actual value.
        return sorted(arr1, key=lambda x: (pos.get(x, len(arr2)), x))
