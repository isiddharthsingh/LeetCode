from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        freq_map = Counter(s)

        # Step 2: Feasibility check: can't rearrange if any char appears too often
        max_allowed = (len(s) + 1) // 2
        for freq in freq_map.values():
            if freq > max_allowed:
                return ""

        # Step 3: Build max heap using negative frequencies
        max_heap = [(-freq, char) for char, freq in freq_map.items()]
        heapq.heapify(max_heap)

        # Track previous character used (to avoid repetition)
        prev_freq, prev_char = 0, ""
        result = []

        # Step 4: Greedily build result string
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            # Push back previous char if still has remaining frequency
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            # Update prev_char and reduce frequency (since it's used once)
            prev_freq = freq + 1  # because freq is negative
            prev_char = char

        return "".join(result)