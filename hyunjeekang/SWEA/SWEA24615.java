import java.util.*;

class UserSolution {
    private static final int MAX_GATE = 201;
    private static final int INF = 1000000000;

    int[][] grid;
    int maxStamina, gridSize;
    
    int[][] gatePos = new int[MAX_GATE][2];    // 게이트 좌표 gatePos[gateID] = {row, col}
    int[][] adj = new int[MAX_GATE][MAX_GATE];    // 인접 행렬 
    boolean[] isActive = new boolean[MAX_GATE];    // 게이트 활성화 여부 저장 

    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};

    void init(int N, int mMaxStamina, int mMap[][]) {
        gridSize = N;
        maxStamina = mMaxStamina;
        grid = new int[N][N];
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                grid[r][c] = mMap[r][c];
            }
        }

        // init
        for (int i = 0; i < MAX_GATE; i++) {
            isActive[i] = false;
            Arrays.fill(adj[i], INF);
            adj[i][i] = 0;
        }
    }

    void addGate(int mGateID, int mRow, int mCol) {
        isActive[mGateID] = true;
        gatePos[mGateID][0] = mRow;
        gatePos[mGateID][1] = mCol;
        grid[mRow][mCol] = mGateID + 10; // 기둥(1)과 Gate(1~200) 구분하기 위해서 +10

        // 새로운 게이트로부터 다른 모든 게이트까지 거리 계산
        bfsDistances(mGateID, mRow, mCol);
    }

    void removeGate(int mGateID) {
        isActive[mGateID] = false;
        int r = gatePos[mGateID][0];
        int c = gatePos[mGateID][1];
        grid[r][c] = 0;
        
        // reset adj 
        Arrays.fill(adj[mGateID], INF);
        adj[mGateID][mGateID] = 0;
        for (int i = 0; i < MAX_GATE; i++) {
            adj[i][mGateID] = INF;
        }
    }

    // bfs : 시작 게이트에서 갈 수 있는 게이트, 거리 찾기 
    private void bfsDistances(int startID, int sr, int sc) {
        Queue<int[]> q = new LinkedList<>();
        int[][] distMap = new int[gridSize][gridSize];
        for(int[] row : distMap) Arrays.fill(row, -1);

        q.add(new int[]{sr, sc});
        distMap[sr][sc] = 0;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int cr = curr[0];
            int cc = curr[1];
            int d = distMap[cr][cc];

            if (grid[cr][cc] >= 10) {
                int targetID = grid[cr][cc] - 10;
                if (isActive[targetID]) {
                    adj[startID][targetID] = d;
                    adj[targetID][startID] = d;
                }
            }
            
            // 더이상 갈 수 없음 ( maxStamina보다 작음 )
            if (d >= maxStamina) continue;

            for (int i = 0; i < 4; i++) {
                int nr = cr + dr[i];
                int nc = cc + dc[i];

                // 테두리가 모두 기둥이라 없어도 됨 
                // if (nr < 0 || nc < 0 || nr >= gridSize || nc >= gridSize) continue;
                if (grid[nr][nc] != 1 && distMap[nr][nc] == -1) {
                    distMap[nr][nc] = d + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
    }
    
    // dijkstra 
    int getMinTime(int mStartGateID, int mEndGateID) {
        int[] minTime = new int[MAX_GATE];
        Arrays.fill(minTime, INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));

        minTime[mStartGateID] = 0;
        pq.add(new int[]{mStartGateID, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int u = curr[0];
            int w = curr[1];

            if (w > minTime[u]) continue;
            if (u == mEndGateID) return w;

            for (int v = 0; v < MAX_GATE; v++) {
                if (isActive[v] && adj[u][v] != INF) {
                    if (minTime[v] > minTime[u] + adj[u][v]) {
                        minTime[v] = minTime[u] + adj[u][v];
                        pq.add(new int[]{v, minTime[v]});
                    }
                }
            }
        }

        return minTime[mEndGateID] == INF ? -1 : minTime[mEndGateID];
    }
}