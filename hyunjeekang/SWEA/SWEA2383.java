import java.io.*;
import java.util.*;

public class SWEA2383 {

    static int N, T, temp, curRes, result, pCnt;

    static boolean[] comb;

    static List<int[]> pCord;
    static List<int[]> sCord;

    static BufferedReader br;
    static StringBuilder sb;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {

            N = Integer.parseInt(br.readLine());

            // map
            pCord = new ArrayList<int[]>();
            sCord = new ArrayList<int[]>();

            for (int r = 0; r < N; r++) {
                st = new StringTokenizer(br.readLine());
                for (int c = 0; c < N; c++) {
                    temp = Integer.parseInt(st.nextToken());
                    if (temp == 1)
                        pCord.add(new int[] { r, c });
                    else if (temp != 0)
                        sCord.add(new int[] { r, c, temp });
                }
            }

            // cnt
            pCnt = pCord.size();
            comb = new boolean[pCnt];

            // reuslt
            result = Integer.MAX_VALUE;
            dfs(0);
            sb.append("#").append(t).append(" ").append(result).append("\n");
        }

        System.out.println(sb);

    }

    /**
     * (4 ≤ N ≤ 10)
     * (1 ≤ pCnt ≤ 10)
     * (2 ≤ 계단의 길이 ≤ 10)
     * 계단의 입구는 반드시 2개
     */

    public static void dfs(int depth) {

        if (depth == pCnt) {

            curRes = simulation();
            result = Math.min(result, curRes);

            return;
        }

        comb[depth] = true;
        dfs(depth + 1);
        comb[depth] = false;
        dfs(depth + 1);

    }

    public static int simulation() {
        ArrayList<Integer> st1arr = new ArrayList<>();
        ArrayList<Integer> st2arr = new ArrayList<>();

        // 계단 사람 도착 시간
        for (int i = 0; i < pCnt; i++) {
            if (comb[i]) {
                st1arr.add(getDist(pCord.get(i)[0], pCord.get(i)[1], sCord.get(0)[0], sCord.get(0)[1]));
            } else {
                st2arr.add(getDist(pCord.get(i)[0], pCord.get(i)[1], sCord.get(1)[0], sCord.get(1)[1]));
            }
        }

        // 각 계단별 소요 시간 계산
        int time1 = calculateStairTime(st1arr, sCord.get(0)[2]);
        int time2 = calculateStairTime(st2arr, sCord.get(1)[2]);

        // 더 늦게 끝나는 계단 시간 리턴
        return Math.max(time1, time2);
    }

    // 계단별 사람들 다 내려가는 시간
    public static int calculateStairTime(ArrayList<Integer> arr, int length) {
        if (arr.isEmpty())
            return 0;

        // 도착 시간 정렬
        Collections.sort(arr);

        int[] finishTime = new int[arr.size()];

        for (int i = 0; i < arr.size(); i++) {
            int arrivalTime = arr.get(i);

            if (i < 3) {
                // 앞 3명 바로 내려감
                finishTime[i] = arrivalTime + 1 + length;
            } else {
                // 이후 사람들은 3칸 앞의 사람이 다 내려간 뒤 진입
                // ( 도착 + 1분 , 3칸 앞 사람이 계단 탈출 시간 중 늦은 시간 ) + 계단 길이
                finishTime[i] = Math.max(arrivalTime + 1, finishTime[i - 3]) + length;
            }
        }

        // 마지막으로 탈출한 사람 시간 리턴
        return finishTime[arr.size() - 1];
    }

    public static int getDist(int sr, int sc, int er, int ec) {
        return Math.abs(sr - er) + Math.abs(sc - ec);
    }
}