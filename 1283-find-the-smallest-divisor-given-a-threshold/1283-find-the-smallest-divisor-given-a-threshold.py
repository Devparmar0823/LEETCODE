import math
from typing import List


class Solution:

  def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    low, high = 1, max(nums)

    while low < high:
      mid = (low + high) // 2
      total_sum = sum((num + mid - 1) // mid for num in nums)

      if total_sum <= threshold:
        high = mid 
      else:
        low = mid + 1 

    return low
