class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        max_freq=max(freq.values())
        count=0
        for num in nums:
            if freq[num]==max_freq:
                count+=1
        return count