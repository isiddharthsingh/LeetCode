class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Convert the bank list to a set for O(1) lookups
        bank_set = set(bank)

        # If the end gene is not in the bank, return -1
        if endGene not in bank_set:
            return -1
        
        # Possible characters for gene mutation
        gene_char = ['A', 'C', 'G', 'T']

        # Initialize the queue with the start gene and 0 steps
        queue = deque([(startGene, 0)])

        while queue:
            curr_gene, steps = queue.popleft()

            # If the current gene is the end gene, return the number of steps
            if curr_gene == endGene:
                return steps
            
            # Try mutating each character in the current gene
            for i in range(len(curr_gene)):
                for char in gene_char:
                    # Skip if the character is the same as the current one
                    if curr_gene[i] == char:
                        continue

                    # Create a new mutated gene
                    mutates_gene = curr_gene[:i] + char + curr_gene[i+1:]

                    # If the mutated gene is in the bank, add it to the queue and remove from the bank
                    if mutates_gene in bank_set:
                        queue.append((mutates_gene, steps + 1))
                        bank_set.remove(mutates_gene)
        
        # If no mutation sequence leads to the end gene, return -1
        return -1