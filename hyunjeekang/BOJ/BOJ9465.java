import java.util.*;
import java.io.*;

public class BOJ9465 {

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        
        for(int t = 0; t < T; t++){
            int N = Integer.parseInt(br.readLine());
            int[][] s = new int[2][N];
            int[][] m = new int[2][N];

            for(int r = 0; r < 2; r++){
                st = new StringTokenizer(br.readLine());
                for(int c = 0; c < N; c++){
                    s[r][c] = Integer.parseInt(st.nextToken());
                }
            }

            m[0][0] = s[0][0];
            m[1][0] = s[1][0];

            for (int c = 1; c < N; c++) {
                m[0][c] = Math.max(m[1][c-1] + s[0][c], m[0][c-1]);
                m[1][c] = Math.max(m[0][c-1] + s[1][c], m[1][c-1]);
            }

            int result = Math.max(m[0][N-1], m[1][N-1]);
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }
}