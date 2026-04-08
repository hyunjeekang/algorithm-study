#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};

struct State {
    int r, c, dir, k;
};

int dist[20][20][4][6];

void solve(int tc) {
    int N, K;
    cin >> N >> K;

    int sr, sc, gr, gc;
    vector<string> board(N);

    for (int i = 0; i < N; i++) {
        cin >> board[i];
        for (int j = 0; j < N; j++) {
            if (board[i][j] == 'X') { sr = i; sc = j; }
            if (board[i][j] == 'Y') { gr = i; gc = j; }
            // 초기화
            for (int d = 0; d < 4; d++) {
                for (int k = 0; k <= K; k++) {
                    dist[i][j][d][k] = -1;
                }
            }
        }
    }

    queue<State> q;
    dist[sr][sc][0][K] = 0;
    q.push({sr, sc, 0, K});

    int answer = -1;

    while (!q.empty()) {
        State cur = q.front();
        q.pop();

        int cur_dist = dist[cur.r][cur.c][cur.dir][cur.k];

        if (cur.r == gr && cur.c == gc) {
            answer = cur_dist;
            break;
        }

        int nr = cur.r + dr[cur.dir];
        int nc = cur.c + dc[cur.dir];

        if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
            if (board[nr][nc] == 'T') { 
                if (cur.k > 0 && dist[nr][nc][cur.dir][cur.k - 1] == -1) {
                    dist[nr][nc][cur.dir][cur.k - 1] = cur_dist + 1;
                    q.push({nr, nc, cur.dir, cur.k - 1});
                }
            } else { 
                if (dist[nr][nc][cur.dir][cur.k] == -1) {
                    dist[nr][nc][cur.dir][cur.k] = cur_dist + 1;
                    q.push({nr, nc, cur.dir, cur.k});
                }
            }
        }

        int next_dir_l = (cur.dir + 3) % 4;
        if (dist[cur.r][cur.c][next_dir_l][cur.k] == -1) {
            dist[cur.r][cur.c][next_dir_l][cur.k] = cur_dist + 1;
            q.push({cur.r, cur.c, next_dir_l, cur.k});
        }

        int next_dir_r = (cur.dir + 1) % 4;
        if (dist[cur.r][cur.c][next_dir_r][cur.k] == -1) {
            dist[cur.r][cur.c][next_dir_r][cur.k] = cur_dist + 1;
            q.push({cur.r, cur.c, next_dir_r, cur.k});
        }
    }

    cout << "#" << tc << " " << answer << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        solve(i);
    }
    return 0;
}