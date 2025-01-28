# Leetcode 1971. Find if Path Exists in Graph
# link: https://leetcode.com/problems/find-if-path-exists-in-graph/



class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        from collections import defaultdict
        def dfs(node: int) -> bool:
            if node == end:
                return True

            if node in visited:
                return False
            visited.add(node)


            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            return False

        graph = defaultdict(list)
        # build graph using adjacency list
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        return dfs(start)