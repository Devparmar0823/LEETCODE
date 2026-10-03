class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        round_time = 2 * (n - 1)
        pos = k % round_time
        return pos if pos < n else round_time - pos