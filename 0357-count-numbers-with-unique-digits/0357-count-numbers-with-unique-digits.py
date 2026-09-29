class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        n = min(n, 10)
        
        total_count = 10
        unique_digits_pool = 9
        current_combinations = 9
        
        for i in range(2, n + 1):
            current_combinations *= unique_digits_pool
            total_count += current_combinations
            unique_digits_pool -= 1
            
        return total_count
