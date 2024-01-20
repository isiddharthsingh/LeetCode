class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0

        for i in nums:
            temp ^= i
        return temp
    
"""
The XOR operation has a special property: for any given number x, x ^ x = 0 and x ^ 0 = x. 
Therefore, if a number appears twice in the list, it will be XORed with itself, resulting in 0. 
This will effectively remove it from temp. If a number appears only once, it will be XORed with 0, so it will remain as it is. 
Therefore, at the end of the loop, temp will hold the number that appears only once in the list.
"""