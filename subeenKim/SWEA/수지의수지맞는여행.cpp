#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int R, C, answer;
bool visited[26];

int backtrack(int x, int y, const vector<vector<char>>& v, int cnt) {
    answer = max(cnt, answer);

    for (int d = 0;d < 4;d++) {
        int nx = x + dx[d], ny = y + dy[d];
        if ((nx >= 0 && nx < R) && (ny >= 0 && ny < C) && (!visited[v[nx][ny] - 'A'])) {
            visited[v[nx][ny] - 'A'] = true;
            backtrack(nx, ny, v, cnt + 1);
            visited [v[nx][ny] - 'A'] = false;
        }
    }
    return answer;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> R >> C;
        vector<vector<char>> v(R, vector<char>(C, ' '));
        for (int i = 0;i < R;i++) {
            for (int j = 0;j < C;j++) {
                cin >> v[i][j];
            }
        }

        
        answer = 0;
        for (int i = 0;i < 26;i++) {
            visited[i] = false;
        }
        visited[v[0][0] - 'A'] = true;
        backtrack(0, 0, v, 1);

        cout << '#' << i << " " << answer << endl;
    }
    return 0;
}