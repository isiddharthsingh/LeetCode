class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If the total number of cards in the hand is not divisible by the group size,
        # it's impossible to form valid groups
        if len(hand) % groupSize:
            return False
        
        count = {}  # Initialize a dictionary to store the count of each card
        for n in hand:
            count[n] = 1 + count.get(n, 0)  # Increment the count for each card

        minHeap = list(count.keys())  # Initialize a min heap with unique card values
        heapq.heapify(minHeap)  # Convert the list to a min heap

        while minHeap:
            first = minHeap[0]  # Get the smallest card value from the heap

            for i in range(first, first + groupSize):
                if i not in count:
                    # If the next card value is not present in the hand, return False
                    return False
                count[i] -= 1  # Decrement the count for the used card
                if count[i] == 0:
                    # If the count becomes zero, remove the card from the heap
                    if i != minHeap[0]:
                        return False  # Ensure the order of cards in the heap
                    heapq.heappop(minHeap)  # Re-heapify after removal

        # If all groups can be formed, return True
        return True
