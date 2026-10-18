class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a=set(nums1)
        b=set(nums2)
        c=a.intersection(b)
        return list(c)
    
