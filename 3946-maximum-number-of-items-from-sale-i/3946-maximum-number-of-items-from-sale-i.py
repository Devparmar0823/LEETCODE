from math import inf
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # dp[j] = max items obtained by buying at most 1 copy of some items with exact cost j
        dp = [0] * (budget + 1)
        min_price = inf
        
        for factor, price in items:
            min_price = min(min_price, price)
            # Count total items gained on first purchase (1 self + all divisible factors)
            gain = sum(1 for other_factor, _ in items if other_factor % factor == 0)
            
            # 0/1 Knapsack transition (iterate backwards)
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + gain)
                
        # Combine first-purchase DP states with buying the cheapest item using leftover budget
        return max(items_gained + (budget - spent) // min_price for spent, items_gained in enumerate(dp))
