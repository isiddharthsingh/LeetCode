class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a dictionary to map each course to its prerequisite list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()  # Set to keep track of visited courses

        def dfs(crs):
            if crs in visited:
                return False  # If we encounter a course that's already visited, there's a cycle
            if preMap[crs] == []:
                return True  # If a course has no prerequisites, it can be completed

            visited.add(crs)  # Mark the current course as visited
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False  # Recursively check prerequisites; if any fails, return False
            visited.remove(crs)  # Remove the current course from visited set
            preMap[crs] = []  # Mark the current course as having no remaining prerequisites
            return True

        # Check all courses for connectivity (graph traversal)
        # for cases where graphs are not linked eg:
        # 1 -> 2
        # 3-> 4
        for crs in range(numCourses):
            if not dfs(crs):
                return False  # If any course cannot be completed, return False

        return True
