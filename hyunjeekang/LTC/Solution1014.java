class Solution {
    public int[][] rotateGrid(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int layers = Math.min(m, n) / 2;

        int maxSize = 2 * (m + n) - 4;
        int[] layer = new int[maxSize];

        for (int l = 0; l < layers; l++) {
            int size = 0;

            // fill layer arr 
            for (int c = l; c < n - l; c++)
                layer[size++] = grid[l][c];
            for (int r = l + 1; r < m - l; r++)
                layer[size++] = grid[r][n - 1 - l];
            for (int c = n - 2 - l; c >= l; c--)
                layer[size++] = grid[m - 1 - l][c];
            for (int r = m - 2 - l; r > l; r--)
                layer[size++] = grid[r][l];

            // rotate
            int p = k % size;
            int i = 0;

            // fill grid
            for (int c = l; c < n - l; c++)
                grid[l][c] = layer[(p + i++) % size];
            for (int r = l + 1; r < m - l; r++)
                grid[r][n - 1 - l] = layer[(p + i++) % size];
            for (int c = n - 2 - l; c >= l; c--)
                grid[m - 1 - l][c] = layer[(p + i++) % size];
            for (int r = m - 2 - l; r > l; r--)
                grid[r][l] = layer[(p + i++) % size];
        }

        return grid;
    }
}