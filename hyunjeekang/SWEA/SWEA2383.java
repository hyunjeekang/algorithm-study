import java.io.*;
import java.util.*;

public class SWEA2383 {

    static int N, T, pCnt;
    static List<int[]> pCord;
    static List<int[]> sCord;
    static int[][] dist; // 거리 미리 계산

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            N = Integer.parseInt(br.readLine());
            
            pCord = new ArrayList<>();
            sCord = new ArrayList<>();

            // 입력
            for (int r = 0; r < N; r++) {
                st = new StringTokenizer(br.readLine());
                for (int c = 0; c < N; c++) {
                    int temp = Integer.parseInt(st.nextToken());
                    if (temp == 1) pCord.add(new int[]{r, c});
                    else if (temp >= 2) sCord.add(new int[]{r, c, temp});
                }
            }
            
            pCnt = pCord.size();
            
            // 거리 미리 계산
            dist = new int[pCnt][2];
            for (int i = 0; i < pCnt; i++) {
                int[] p = pCord.get(i);
                int[] s1 = sCord.get(0);
                int[] s2 = sCord.get(1);
                dist[i][0] = Math.abs(p[0] - s1[0]) + Math.abs(p[1] - s1[1]);
                dist[i][1] = Math.abs(p[0] - s2[0]) + Math.abs(p[1] - s2[1]);
            }

            int result = Integer.MAX_VALUE;
            
            // 비트마스킹
            int totalCases = 1 << pCnt;
            for (int mask = 0; mask < totalCases; mask++) {
                result = Math.min(result, simulation(mask));
            }

            sb.append("#").append(t).append(" ").append(result).append("\n");
        }
        System.out.println(sb);
    }

    // 시뮬레이션
    public static int simulation(int mask) {
        int[] q1 = new int[pCnt];
        int[] q2 = new int[pCnt];
        int idx1 = 0, idx2 = 0;

        // 마스크 확인 -> 계단 분기
        for (int i = 0; i < pCnt; i++) {
            // i번째 비트가 1이면 1번 계단, 0이면 2번 계단
            if ((mask & (1 << i)) != 0) {
                q1[idx1++] = dist[i][0];
            } else {
                q2[idx2++] = dist[i][1];
            }
        }

        int time1 = calculateStairTime(q1, idx1, sCord.get(0)[2]);
        int time2 = calculateStairTime(q2, idx2, sCord.get(1)[2]);

        return Math.max(time1, time2);
    }

    // 계단 소요 시간 계산
    public static int calculateStairTime(int[] arr, int len, int stairLength) {
        if (len == 0) return 0;
        
        // 들어온 사람 수(len) 만큼만 정렬
        Arrays.sort(arr, 0, len);
        
        int[] finishTime = new int[len];
        
        for (int i = 0; i < len; i++) {
            int arrivalTime = arr[i];
            
            if (i < 3) {
                finishTime[i] = arrivalTime + 1 + stairLength;
            } else {
                finishTime[i] = Math.max(arrivalTime + 1, finishTime[i - 3]) + stairLength;
            }
        }
        
        return finishTime[len - 1];
    }
}