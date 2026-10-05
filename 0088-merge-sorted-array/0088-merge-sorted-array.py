class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=len(nums1)-1
        while nums2:
            nums1[i]=nums2[-1]
            nums2.remove(nums2[-1])
            i-=1
        nums1.sort()
        return nums1