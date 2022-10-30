def numIslands(self, grid: List[List[str]]) -> int:
    def infection(i, j, row, col, grid):
        # if (i < 0 or j < 0 or i >= row or j >= col or grid[i][i] == '0'):
        #     return                                          #没懂这里为什么是错的
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return
        grid[i][j] = '0'
        infection(i - 1, j, row, col, grid)
        infection(i + 1, j, row, col, grid)
        infection(i, j - 1, row, col, grid)
        infection(i, j + 1, row, col, grid)

    row = len(grid)
    col = len(grid[0])
    res = 0

    for i in range(row):
        for j in range(col):
            if (grid[i][j] == '1'):
                res += 1
                infection(i, j, row, col, grid)

    return res