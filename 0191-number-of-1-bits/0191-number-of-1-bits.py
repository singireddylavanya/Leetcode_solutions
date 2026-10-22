class Solution:
    def hammingWeight(self, n: int) -> int:
        binary=""
        while n>0:
            r=n%2
            binary=str(r)+binary
            n=n//2
        res=binary
        return res.count("1")
        