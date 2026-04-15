import java.io.*;
import java.util.*;

public class BOJ1932 {

    static int N;
    static int[][] tri, memo;

    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        tri = new int[N][N];
        memo = new int[N][N];
        for(int i = 0 ; i < N; i++){
            Arrays.fill(memo[i], -1);
        }

        for(int i = 0 ; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < i+1; j++){
                tri[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int result = Integer.MIN_VALUE;
        for(int i = 0 ; i < N; i++){
            result = Math.max(result, recur(N-1, i));
        }

        System.out.println(result);
    }

    private static int recur(int r, int c){

        if(!inBounds(r, c)) return 0;

        if(r == 0 && c == 0) return memo[r][c] = tri[r][c];

        if(memo[r][c] != -1) return memo[r][c];

        return memo[r][c] = Math.max(recur(r-1, c), recur(r-1, c-1)) + tri[r][c];

    }

    private static boolean inBounds(int r, int c){
        return 0 <= r && r < N && 0 <= c && c < N;
    }
}
