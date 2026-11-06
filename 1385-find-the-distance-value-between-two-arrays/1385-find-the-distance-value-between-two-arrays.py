class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        for x in arr1:
            is_valid = True
            for num in arr2:
                if abs(x - num) <= d:
                    is_valid = False
                    break 
            if is_valid:
                ans += 1
        return ans
