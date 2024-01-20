class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        div = 1
        #if number is 121 then add zeros to div 
        while x >= 10*div:
            div *= 10

        while x:
            if x // div != x%10: return False
            #get rid of first and last digit
            x = (x%div) // 10 
            #chop off two digits
            div = div / 100
        return True
