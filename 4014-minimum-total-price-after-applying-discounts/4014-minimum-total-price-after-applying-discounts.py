class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        i=0
        while discounts and i<len(prices):
            prices[i]=(prices[i]*(100-discounts[0]))/100
            discounts.remove(discounts[0])
            i+=1
        return sum(prices)