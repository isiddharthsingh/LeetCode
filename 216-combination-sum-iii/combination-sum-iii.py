class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb, total):
            # Base case: if we have k numbers
            if len(comb) == k:
                if total == n:
                    res.append(comb[:])
                return

            for i in range(start, 10):  # numbers 1 to 9
                if total + i > n:
                    break  # prune the path early
                comb.append(i)
                backtrack(i + 1, comb, total + i)  # use i+1 to avoid reuse
                comb.pop()  # backtrack

        backtrack(1, [], 0)
        return res