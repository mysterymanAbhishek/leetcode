class Solution(object):
    def rotate(self, nums, k):
        # Handle cases where k is greater than the length of nums
        k = k % len(nums)
        
        # Helper function to reverse elements in the array
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        
        # Step 1: Reverse the entire array
        reverse(nums, 0, len(nums) - 1)
        
        # Step 2: Reverse the first k elements
        reverse(nums, 0, k - 1)
        
        # Step 3: Reverse the remaining elements
        reverse(nums, k, len(nums) - 1)

        