class RandomizedSet:
    def __init__(self):
        # Initialize an empty dictionary to store values and their indices
        self.numMap = {}
        # Initialize an empty list to store values
        self.numList = []

    def insert(self, val: int) -> bool:
        # Check if the value is not already in the dictionary
        res = val not in self.numMap
        if res:
            # Add the value to the dictionary with its index in the list
            self.numMap[val] = len(self.numList)
            # Append the value to the list
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        # Check if the value is in the dictionary
        res = val in self.numMap
        if res:
            # Get the index of the value
            idx = self.numMap[val]
            # Swap the value with the last value in the list
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            # Update the index of the last value in the dictionary
            self.numMap[lastVal] = idx
            # Remove the value from the dictionary
            del self.numMap[val]
            # Remove the last value from the list
            self.numList.pop()
        return res

    def getRandom(self) -> int:
        # Return a random value from the list
        return random.choice(self.numList)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()