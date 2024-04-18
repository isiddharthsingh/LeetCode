class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        freq_sorted = sorted(freq.values(), reverse=True)
        print(freq_sorted)
        
        count, size = 0, 0
        half_size = len(arr) // 2
        
        for f in freq_sorted:
            count += f
            size += 1
            if count >= half_size:
                return size

