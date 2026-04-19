import java.io.*;
import java.util.*;

public class BOJ1389 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력
        int N, M, INF, result;
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // 초기화
        INF = 10000;
        int[][] adj = new int[N + 1][N + 1];
        for (int i = 0; i <= N; i++) {
            Arrays.fill(adj[i], INF);
            adj[i][i] = 0;
        }

        // 인접행렬 입력
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adj[a][b] = 1;
            adj[b][a] = 1;
        }

        // 1. fw
        // result = fw(adj, N, INF);
        // 2. bfs
        result = bfs(adj, N, INF);

        System.out.println(result);
    }

    private static int fw(int[][] adj, int N, int INF) {
        int minP, minV, curV;

        // 플로이드워셜
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    adj[i][j] = Math.min(adj[i][j], (adj[i][k] + adj[k][j]));
                }
            }
        }

        // 최소 확인하기
        minV = INF;
        minP = 0;
        for (int p = 1; p <= N; p++) {
            curV = Arrays.stream(adj[p])
                    .filter(value -> value != INF)
                    .sum();

            if (curV < minV) {
                minV = curV;
                minP = p;
            } else if (curV == minV) {
                if (p < minP)
                    minP = p;
            }
        }

        return minP;
    }

    private static int bfs(int[][] adj, int N, int INF) {
        int minP = 0, minV = INF, curV = 0;

        for (int p = 1; p <= N; p++) {
            Queue<int[]> q = new LinkedList<>();
            int[] dist = new int[N + 1];
            Arrays.fill(dist, INF);

            dist[p] = 0;
            q.offer(new int[] { p, 0 });

            while (!q.isEmpty()) {
                int[] cur = q.poll();
                for (int i = 1; i <= N; i++) {
                    if (adj[cur[0]][i] == 1 && dist[i] == INF) {
                        dist[i] = cur[1] + 1;
                        q.offer(new int[] { i, dist[i] });
                    }
                }
            }

            curV = 0;
            for (int i = 1; i <= N; i++) {
                if (dist[i] != INF) {
                    curV += dist[i];
                }
            }

            if (curV < minV) {
                minV = curV;
                minP = p;
            } else if (curV == minV) {
                if (p < minP) {
                    minP = p;
                }
            }

        }

        return minP;
    }
}
