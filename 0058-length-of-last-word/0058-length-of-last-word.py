class Solution(object):
    def lengthOfLastWord(self, s): 
        lst=s.split()
        if(len(lst)==0):
            return 0
        return len(lst[-1])
      
        