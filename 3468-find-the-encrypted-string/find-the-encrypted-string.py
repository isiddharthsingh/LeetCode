class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k = k%n
        res = ""
        for i in range(n):
            res+= s[(i+k)%n]
        return res