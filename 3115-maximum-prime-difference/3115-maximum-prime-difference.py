class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5+1)):
                if n%i==0:
                    return False
            return True
        left=0
        right=len(nums)-1
        while left<len(nums) and not is_prime(nums[left]):
            left+=1
        while right>=0 and not is_prime(nums[right]):
            right-=1
        return right-left    