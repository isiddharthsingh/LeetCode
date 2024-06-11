class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort in descending order
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h += 1
            else:
                break
        return h
