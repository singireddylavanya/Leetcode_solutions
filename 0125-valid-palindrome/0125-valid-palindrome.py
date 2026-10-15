class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for ch in s:
            if ch.isupper():
                ans+=ch.lower()
            elif ch.isalnum():
                ans+=ch
            
        return ans==ans[::-1]           
