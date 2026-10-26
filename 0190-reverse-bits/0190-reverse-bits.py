class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:].zfill(32)
        binary=n[::-1]
        return(int(binary,2))
    