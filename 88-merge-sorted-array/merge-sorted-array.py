class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        for j in range(n):
            nums1[i] = nums2[j]
            i += 1

        nums1.sort()

        return nums1

        