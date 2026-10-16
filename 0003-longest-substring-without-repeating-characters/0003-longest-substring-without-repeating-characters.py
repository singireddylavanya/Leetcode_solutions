class Solution:
    def lengthOfLongestSubstring(self, s):
        a=set()
        j=0
        max_len=0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[j])
                j+=1
            a.add(s[i])
            b=len(s[j:i+1]) 
            max_len=max(max_len,b)      
        return(max_len)        
      
        
                     




        
      

        
       