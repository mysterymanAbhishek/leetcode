class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        j=0
        
        for i in range(1,len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
        return j+1
        
        