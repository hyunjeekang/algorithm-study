import java.io.*;
import java.util.*;

public class BOJ9465 {
    
    static int T, N;
    
    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args)  throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++){
            
            N = Integer.parseInt(br.readLine());
            int[][] s = new int[2][N];
            int[][] m = new int[2][N];

            for(int i = 0 ; i < 2; i++){
                Arrays.fill(m[i], -1);
            }

            for(int r = 0; r < 2; r++){
                st = new StringTokenizer(br.readLine());
                for(int c = 0; c < N; c++){
                    s[r][c] = Integer.parseInt(st.nextToken());
                }
            }

            int result = Math.max(dp(s, m, 0, N-1), dp(s, m, 1, N-1));
            sb.append(result).append("\n");
        }
        System.out.println(sb);
    }

    private static int dp(int[][] s, int[][] m, int r, int c){
        
        if(c < 0) return 0;

        if(c == 0) return s[r][c];

        if(m[r][c] != -1) return m[r][c];

        // 선택 안 하고 주변값가져오는 경우 추가해야함
        if(r == 0) m[r][c] = dp(s, m, r+1, c-1) + s[r][c];
        else m[r][c] = dp(s, m, r-1, c-1) + s[r][c];
        
        return m[r][c];
    }
}
