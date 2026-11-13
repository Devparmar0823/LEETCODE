class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in nums[:]:
            if freq[num] > 2:
                nums.remove(num)
                freq[num] -= 1
        return len(nums)