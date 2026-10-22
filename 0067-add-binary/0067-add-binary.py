class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=0
        for digit in a:
            n=n*2+int(digit)
        s=0
        for digit in b:
            s=s*2+int(digit)
        res=n+s
        return(bin(res)[2:])          
        