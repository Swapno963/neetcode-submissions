class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start working with the num2 array
        for i in range(n):
            j = 0
            while nums1[j] < nums2[i] and j < m + i:
                j += 1
            # Shift the elements to the right
            nums1.insert(j, nums2[i])
            nums1.pop()  # Remove the last element to maintain the size
