class Solution:
    def merge(self, nums1, m, nums2, n):
        k = m + n - 1  # Merge position, starting from the end
        i, j = m - 1, n - 1  # Last elements of nums1 and nums2
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
