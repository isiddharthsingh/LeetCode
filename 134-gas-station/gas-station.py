class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total gas available is less than the total cost, it's impossible to complete the circuit
        if sum(gas) < sum(cost):
            return -1
        
        total = 0  # Initialize the total gas balance
        res = 0  # Initialize the starting index of the circuit

        for i in range(len(gas)):
            total += (gas[i] - cost[i])  # Update the gas balance by considering the difference

            if total < 0:
                # If the gas balance becomes negative, reset it to zero and update the starting index
                total = 0
                res = i + 1

        return res
