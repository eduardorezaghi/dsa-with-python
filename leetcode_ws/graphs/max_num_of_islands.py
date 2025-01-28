# Leetcode 695. Max Area of Islands
# link:


class Solution:
    positions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1)  # right
    ]
    
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(r: int, c: int):
            if r < 0 or r >= ROWS or\
               c < 0 or c >= COLS or\
               grid[r][c] == 0 or\
               (r,c) in visited:
                   return 0
        
            visited.add((r,c))

            acc = 1
            acc += sum(dfs(r + dr, c + dc) for dr, dc in Solution.positions)
            return acc

        max_area = 0
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(max_area, dfs(row, col))
        
        return max_area

if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland(
        [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
    )) # 6