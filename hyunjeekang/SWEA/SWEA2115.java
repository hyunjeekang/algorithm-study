import java.util.*;
import java.io.*;
 
public class SWEA2115 {
     
    static int res;
    static boolean[][] visited;
     
    public static void main(String[] args) throws IOException{
         
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         
        int T = Integer.parseInt(br.readLine());
        int[][] map = new int[11][11];
         
        for(int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());
             
            for(int r = 0 ; r < N; r++) {
                st = new StringTokenizer(br.readLine());
                for(int c = 0; c < N; c++) {
                    map[r][c] = Integer.parseInt(st.nextToken());
                }
            }
             
            res = 0;
            visited = new boolean[N][N];
             
            solve(0, 0, 0, N, M, C, map);
            sb.append("#").append(t).append(" ").append(res).append("\n");
        }
        System.out.println(sb);
    }
     
    public static void  solve(int ppl, int sr, int prof, int N, int M, int C, int[][] map) {
        if(ppl == 2) {
            res = res >= prof ? res : prof;
            return;
        }
         
        for(int r = sr; r < N; r++) {
             
            for(int c = 0; c <= N - M; c++) {
                boolean available = true;
                for(int i = 0; i < M; i++) {
                     
                    if(visited[r][c+i]) {
                        available = false;
                        break;
                    }
                }
                 
                if(available) {
                    for(int i = 0 ; i < M; i++) {
                        visited[r][c+i] = true;
                    }
                     
                    int curProf = getMaxProf(r, c, M, C, map);
                     
                    solve(ppl+1, r, curProf + prof, N, M, C, map);
                     
                    for(int i = 0 ; i < M; i++) {
                        visited[r][c+i] = false;
                    }
                }
            }
        }
    }
     
    public static int getMaxProf(int r, int c, int M, int C, int[][] map) {
        int maxProf = 0;
        int subsets = 1 << M;
         
        for(int mask = 0; mask < subsets; mask++) {
            int honey = 0;
            int prof = 0;
             
            for(int i = 0; i < M; i++) {
                if((mask & ( 1 << i)) != 0) {
                    int h = map[r][c+i];
                    honey += h;
                    prof += h * h;
                }
            }
             
            if(honey <= C) {
                maxProf = maxProf > prof ? maxProf : prof; 
            }
        }
        return maxProf;
    }
  
    /**
     * 두 명의 일꾼은 각각
     * 가로로 연속되도록 M개의 벌통을 선택
         * 두 일꾼이 선택한 벌통이 서로 겹치면 안 됨
         * M개 벌꿀 합은 C 이하
         * 수익 : 각 용기**2 합
           
     * 1. 겹치지 않게 조합 구하기
     * 2. 조건 만족하는지 확인
     * 3. 수익 계산
     * 4. 이전 최대 수익값과 비교, 갱신
     * */
}