class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a dictionary to store prerequisites for each course
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []  # List to store the order of courses
        visit, cycle = set(), set()  # Sets to track visited courses and detect cycles

        def dfs(crs):
            if crs in cycle:
                return False  # If we encounter a cycle, return False
            if crs in visit:
                return True  # If the course is already visited, it's safe

            cycle.add(crs)  # Mark the current course as part of the current DFS path
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False  # Recursively check prerequisites; if any fails, return False
            cycle.remove(crs)  # Remove the current course from the DFS path
            visit.add(crs)  # Mark the course as visited
            output.append(crs)  # Add the course to the output list
            return True

        # Check all courses for connectivity (graph traversal)
        for c in range(numCourses):
            if not dfs(c):
                return []  # If any course cannot be completed, return an empty list

        return output
