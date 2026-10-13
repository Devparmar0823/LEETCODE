class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        i=0
        while coins>0 and i<len(costs):
            if coins<costs[i]:
                return i
            coins-=costs[i]
            i+=1
        return i