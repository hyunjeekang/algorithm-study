import java.util.*;
import java.io.*;

public class SWEA5648 {

    static class Atom {
        int x, y, dx, dy, energy;

        static final int[] DX = { 0, 0, -1, 1 };
        static final int[] DY = { 1, -1, 0, 0 };

        Atom(int x, int y, int dir, int energy) {
            this.x = x;
            this.y = y;
            this.dx = DX[dir];
            this.dy = DY[dir];
            this.energy = energy;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());

            Atom[] atoms = new Atom[N];
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int dir = Integer.parseInt(st.nextToken());
                int k = Integer.parseInt(st.nextToken());
                atoms[i] = new Atom(x, y, dir, k);
            }

            // 충돌 시간, 충돌 워자 리스트
            Map<Integer, List<int[]>> map = new TreeMap<>();

            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    Atom a = atoms[i], b = atoms[j];

                    int ddx = a.dx - b.dx;
                    int ddy = a.dy - b.dy;
                    int rx = b.x - a.x;
                    int ry = b.y - a.y;

                    Integer t2 = null;

                    /**
                     * 충돌 : 특정 위치에 같은 시간에 도달해야 함
                     * 거리를 속도(방향*1)으로 나누어서 시간 계산
                     * 시간이 양수라면 미래에 충돌 
                     * 두 원자가 홀수칸 떨어져 있으면 소숫점 처리 해야해서 2 곱하기
                     */
                    
                    // 이동 방향이 같은 경우
                    if (ddx == 0 && ddy == 0) {
                        continue;
                    
                    // y 방향만 다른 경우 
                    } else if (ddx == 0) {
                        if (rx != 0)    // x좌표 다르면 평행이라 안 만남 
                            continue;
                        t2 = 2 * ry / ddy;
                    
                    // x 방향만 다른 경우 
                    } else if (ddy == 0) {
                        if (ry != 0)
                            continue;
                        t2 = 2 * rx / ddx;

                    // x y 방향 모두 다른 경우 
                    } else {
                        if (rx * ddy != ry * ddx) // 충돌 안 하는 경우
                            continue;
                        t2 = 2 * rx / ddx;
                    }
                    
                    // 충돌 시간, 충돌 원자 리스트 
                    if (t2 != null && t2 > 0) {
                        map.computeIfAbsent(t2, k -> new ArrayList<>()).add(new int[] { i, j });
                    }
                }
            }

            // 처리
            boolean[] live = new boolean[N];
            Arrays.fill(live, true);
            int totalEnergy = 0;

            for (List<int[]> pairs : map.values()) {
                Set<Integer> die = new HashSet<>();

                for (int[] pair : pairs) {
                    int i = pair[0], j = pair[1];
                    if (live[i] && live[j]) { // 앞에서 처리한 원자가 아닐 때 충돌 처리 
                        die.add(i);
                        die.add(j);
                    }
                }

                for (int idx : die) {
                    live[idx] = false;
                    totalEnergy += atoms[idx].energy;
                }
            }

            sb.append("#").append(tc).append(" ").append(totalEnergy).append("\n");
        }

        System.out.print(sb);
    }
}