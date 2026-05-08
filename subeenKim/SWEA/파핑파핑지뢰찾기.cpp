#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int finding_bomb() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int N, answer = 0;
        cin >> N;
        vector<vector<char>> v(N, vector<char>(N, '0'));
        vector<vector<int>> bomb(N, vector<int>(N, 0));
        vector<vector<bool>> visited(N, vector<bool>(N, false));

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                cin >> v[x][y];
            }
        }

        int dx[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
        int dy[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };

        //주변 지뢰 개수 저장. 해당 칸이 지뢰이면 -1 저장
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                if (v[x][y] == '*') {
                    bomb[x][y] = -1;
                }
                else {
                    for (int d = 0; d < 8;d++) {
                        int nx = x + dx[d], ny = y + dy[d];
                        if ((nx >= 0 && nx < N) && (ny >= 0 && ny < N) && (v[nx][ny] == '*')) {
                            bomb[x][y]++;
                        }
                    }
                }
            }
        }

        //0인 칸에 대해서 bfs 수행
        queue<pair<int, int>> q;
        for (int r = 0;r < N;r++) {
            for (int c = 0;c < N;c++) {
                if (bomb[r][c] == 0 && !visited[r][c]) {
                    q.push({ r, c });
                    while (!q.empty()) {
                        int x = q.front().first, y = q.front().second;
                        q.pop();
                        for (int d = 0;d < 8;d++) {
                            int nx = x + dx[d], ny = y + dy[d];
                            if ((nx >= 0 && nx < N) && (ny >= 0 && ny < N) && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                if (bomb[nx][ny] == 0) {
                                    q.push({ nx, ny });
                                }
                            }
                        }
                    }
                    answer++;
                }
            }
        }

        for (int x = 0;x < N;x++) {
            for (int y = 0;y < N;y++) {
                if (!visited[x][y] && bomb[x][y] > 0) {
                    answer++;
                }
            }
        }

        cout << '#' << i << " " << answer << endl;
    }
    return 0;
}