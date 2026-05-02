import java.io.*;
import java.util.*;

public class SWEA1868 {

    static BufferedReader br;
    static StringBuilder sb = new StringBuilder();

    static final int[] drs = { -1, -1, -1, 0, 0, 1, 1, 1 };
    static final int[] dcs = { -1, 0, 1, -1, 1, -1, 0, 1 };

    static int T, N, cnt;
    static char[][] map;
    static int[][] cntMap;
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        if (input == null) return;
        
        T = Integer.parseInt(input);

        for (int t = 1; t <= T; t++) {
            N = Integer.parseInt(br.readLine());
            map = new char[N][N];
            cntMap = new int[N][N];
            visited = new boolean[N][N];
            cnt = 0; 
            
            for (int r = 0; r < N; r++) {
                map[r] = br.readLine().toCharArray();
            }

            // 8칸 지뢰 개수 계산 
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    if (map[r][c] == '*') {
                        cntMap[r][c] = -1; // 지뢰
                        continue;
                    }
                    int mineCount = 0;
                    for (int i = 0; i < 8; i++) {
                        int nr = r + drs[i];
                        int nc = c + dcs[i];
                        if (inBounds(nr, nc) && map[nr][nc] == '*') {
                            mineCount++;
                        }
                    }
                    cntMap[r][c] = mineCount;
                }
            }

            // 0칸부터 
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                	// 범위 내 + 아직 방문하지 않은 빈칸
                    if (cntMap[r][c] == 0 && !visited[r][c] && map[r][c] == '.') {
                        cnt++;
                        bfs(r, c);
                    }
                }
            }

            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    if (map[r][c] == '.' && !visited[r][c]) {
                        cnt++;
                    }
                }
            }

            sb.append('#').append(t).append(' ').append(cnt).append('\n');
        }
        System.out.print(sb);
    }

    public static void bfs(int sr, int sc) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] { sr, sc });
        visited[sr][sc] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cr = cur[0];
            int cc = cur[1];

            // 0인 경우 큐에 넣기 
            if (cntMap[cr][cc] == 0) {
                for (int i = 0; i < 8; i++) {
                    int nr = cr + drs[i];
                    int nc = cc + dcs[i];

                    // 범위 내 + 아직 방문하지 않은 빈칸
                    if (inBounds(nr, nc) && !visited[nr][nc] && map[nr][nc] == '.') {
                        visited[nr][nc] = true;
                        q.add(new int[] { nr, nc });
                    }
                }
            }
        }
    }

    public static boolean inBounds(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < N;
    }
}