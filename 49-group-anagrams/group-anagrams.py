from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a default dictionary to group the anagrams
        res = defaultdict(list)

        # Iterate over each string in the input list
        for s in strs:
            # Initialize a list to count the occurrences of each character
            count = [0] * 26
            

            # Count the occurrences of each character in the string
            for c in s:
                count[ord(c) - ord("a")] += 1
                #print(count)

            # Add the string to the group of its anagrams
            # Anagrams will have the same counts for each character
            res[tuple(count)].append(s)
        print(res)
        
        # Return the groups of anagrams
        return res.values()
