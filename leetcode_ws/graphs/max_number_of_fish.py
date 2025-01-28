# Leetcode 2658. Max Number of Fish
# link: https://leetcode.com/problems/max-number-of-fish/

class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        def dfs(row: int, column: int) -> int:
            if row < 0 or row >= ROWS or\
                column < 0 or column >= COLS or\
                grid[row][column] == 0 or\
                visited[row][column]:
                return 0

            # here, we're garanteed that grid[row][column] is "1" and within bounds
            # Check all 4 directions for "1" and mark them as "0"
            # - Up (row - 1, column)
            # - Down (row + 1, column)
            # - Left (row, column - 1)
            # - Right (row, column + 1)

            visited[row][column] = True

            res = grid[row][column]
            acc = res + (
                # up
                dfs(row - 1, column) +
                # down
                dfs(row + 1, column) +
                # left
                dfs(row, column - 1) +
                # right
                dfs(row, column + 1)
            )
            return acc

        num_fishes = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        for row in range(ROWS):
            for column in range(COLS):
                if grid[row][column] > 0:
                    # greedy approach: we're looking for the maximum number of fishes in a contiguous area of water.
                    num_fishes = max(num_fishes, dfs(row, column))
        return num_fishes

if __name__ == "__main__":
    # Example 1:
    # Input: grid = [
    #     [0,2,1,0],
    #     [4,0,0,3],
    #     [1,0,0,4],
    #     [0,3,2,0],
    # ]
    # Output: 7
    print(Solution().maxNumberOfFishes([
        [0,2,1,0],
        [4,0,0,3],
        [1,0,0,4],
        [0,3,2,0],
    ]))  # 7
