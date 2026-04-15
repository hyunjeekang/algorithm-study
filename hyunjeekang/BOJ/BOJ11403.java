import java.io.*;
import java.util.*;

public class BOJ11403 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int INF = 100;
        int[][] adj = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                adj[i][j] = Integer.parseInt(st.nextToken()) == 1 ? 1 : INF;

            }
        }

        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    adj[i][j] = Math.min(adj[i][j], (adj[i][k] + adj[k][j]));
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int data = adj[i][j] < INF ? 1 : 0;
                sb.append(data).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);

    }

}
