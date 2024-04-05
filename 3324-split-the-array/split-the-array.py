class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = {}

        for n in nums:
            counter[n] = counter.get(n,0) + 1

        for count in counter.values():
            if count >2:
                return False
        return True