#include <iostream>
#include <queue>

using namespace std;

const int num2dir[8] = { 0, 15, 10, 5, 9, 3, 6, 12 };

const int dr[4] = { 0, 1, 0, -1 };
const int dc[4] = { 1, 0, -1, 0 };

struct Node {
    int r;
    int c;
    int time;
};

inline bool is_valid(int r, int c, int N, int M) {
    return (r >= 0 && r < N && c >= 0 && c < M);
}

inline bool can_connect(int cur_pipe, int next_pipe, int dir) {
    if (next_pipe == 0) return false; 

    int cur_open = (1 << dir) & num2dir[cur_pipe];
    int next_open = (1 << ((dir + 2) % 4)) & num2dir[next_pipe];

    return (cur_open && next_open);
}

int bfs(int N, int M, int R, int C, int L, int arr[50][50]) {
    bool visited[50][50] = { false };
    int pipe_cnt = 1;

    queue<Node> q;

    visited[R][C] = true;
    q.push({ R, C, 1 }); 

    while (!q.empty()) {
        Node cur = q.front();
        q.pop();

        if (cur.time == L) continue;

        for (int dir = 0; dir < 4; ++dir) {
            int nr = cur.r + dr[dir];
            int nc = cur.c + dc[dir];

            if (!is_valid(nr, nc, N, M)) continue;                 // 1. 범위 밖이면 패스
            if (visited[nr][nc]) continue;                         // 2. 이미 방문했으면 패스
            if (!can_connect(arr[cur.r][cur.c], arr[nr][nc], dir)) continue; // 3. 연결 안 되면 패스

            visited[nr][nc] = true;
            pipe_cnt++;
            q.push({ nr, nc, cur.time + 1 });
        }
    }

    return pipe_cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        int N, M, R, C, L;
        cin >> N >> M >> R >> C >> L;

        int arr[50][50];

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                cin >> arr[r][c];
            }
        }

        int answer = bfs(N, M, R, C, L, arr);

        cout << "#" << test_case << " " << answer << "\n";
    }

    return 0;
}