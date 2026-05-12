import java.util.ArrayList;
import java.util.List;

class Solution1014 {
    public int[][] rotateGrid(int[][] grid, int k) {
        int n = grid[0].length;
        int m = grid.length;
        int layers = Math.min(m, n) / 2;
        List<Integer> layer = new ArrayList<>();

        for (int l = 0; l < layers; l++) {
            layer.clear();

            // top
            for (int c = l; c < n - l; c++) 
                layer.add(grid[l][c]);
            // right
            for (int r = l + 1; r < m - l; r++)
                layer.add(grid[r][n - 1 - l]);
            // bottom
            for (int c = n - 2 - l; c >= l; c--)
                layer.add(grid[m - 1 - l][c]);
            // left
            for (int r = m - 2 - l; r > l; r--)
                layer.add(grid[r][l]);

            int s = layer.size();
            int p = k % s;
            int i = 0;

            // top
            for (int c = l; c < n - l; c++)
                grid[l][c] = layer.get((p + i++) % s);
            // right
            for (int r = l + 1; r < m - l; r++)
                grid[r][n - 1 - l] = layer.get((p + i++) % s);
            // bottom
            for (int c = n - 2 - l; c >= l; c--)
                grid[m - 1 - l][c] = layer.get((p + i++) % s);
            // left
            for (int r = m - 2 - l; r > l; r--)
                grid[r][l] = layer.get((p + i++) % s);
        }

        return grid;
    }
}