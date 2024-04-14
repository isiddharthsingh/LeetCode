class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count = 0 
        amount.sort(reverse=True)

        while amount[0] > 0:
            if amount[1] > 0:
                amount[0] -= 1
                amount[1] -= 1
            else:
                amount[0] -=1
            count+=1
            amount.sort(reverse=True)
        return (count)