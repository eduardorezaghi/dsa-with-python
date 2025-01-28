# Leetcode: 200. Number of Islands
# link: https://leetcode.com/problems/number-of-islands/

class Solution:
    positions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }
    
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(row: int, column: int) -> None:
            # Base case so that we don't go out of bounds:
            # - row is out of bounds (leftmost or rightmost)
            # - column is out of bounds (topmost or bottommost)
            # - grid[row][column] is "0"
            # in all these cases, do nothing.
            
            if  row < 0 or row >= len(grid) or\
                column < 0 or column >= len(grid[0]) or\
                grid[row][column] == "0":
                return
            # here, we're garanteed that grid[row][column] is "1" and within bounds

            # Check all 4 directions for "1" and mark them as "0"
                # - Up (row - 1, column)
                # - Down (row + 1, column)
                # - Left (row, column - 1)
                # - Right (row, column + 1)
            grid[row][column] = "0"
            for pos in self.positions.values():
                dfs(row + pos[0], column + pos[1])
        
        num_islands = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    num_islands += 1
                    dfs(row, column)
        return num_islands

if __name__ == "__main__":
    # Example 1:
    # Input: grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    # Output: 1
    print(Solution().numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))  # 1

    # Example 2:
    # Input: grid = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]
    # Output: 3
    print(Solution().numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))  # 3