class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        if sum(diffs) <= k:
            return 0    
        buckets = [0] * (max_diff + 1)
        for d in diffs:
            buckets[d] += 1
        for d in range(max_diff, 0, -1):
            if buckets[d] > 0:
                use = min(buckets[d], k)
                buckets[d] -= use
                buckets[d - 1] += use
                k -= use
                if k == 0:
                    break
        return sum(count * (d ** 2) for d, count in enumerate(buckets))