class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        p=prices[0]+prices[1]
        if p>money:
            return money
        return abs(p-money)