class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays, nums1 and nums2, where nums1 has enough space to hold the additional elements from nums2.
        Do not return anything, modify nums1 in-place instead.

        :param nums1: List[int] - First sorted array with m elements followed by n empty spaces.
        :param m: int - Number of valid elements in nums1.
        :param nums2: List[int] - Second sorted array with n elements.
        :param n: int - Number of elements in nums2.
        """
        # Last index of merged array
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            # Compare the last elements of nums1 and nums2
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]  # Move the larger element to the end of nums1
                m -= 1  # Decrement m as we've used one element from nums1
            else:
                nums1[last] = nums2[n - 1]  # Move the larger element to the end of nums1
                n -= 1  # Decrement n as we've used one element from nums2
            last -= 1  # Move to the next position for merging

        # Fill nums1 with leftover elements from nums2, if any
        while n > 0:
            nums1[last] = nums2[n - 1]  # Move the remaining elements from nums2 to nums1
            n, last = n - 1, last - 1  # Decrement n and last
