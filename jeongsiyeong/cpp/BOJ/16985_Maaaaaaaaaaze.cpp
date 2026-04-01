#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <cstring>

using namespace std;

int dr[6] = {1, 0, -1, 0, 0, 0};
int dc[6] = {0, 1, 0, -1, 0, 0};
int dz[6] = {0, 0, 0, 0, 1, -1};

int rotated_boards[5][4][5];

int bfs(int maze[5][5]) {
    int visited[5][5][5];
    memset(visited, -1, sizeof(visited));
    
    queue<tuple<int, int, int>> q;
    q.push({0, 0, 0});
    visited[0][0][0] = 0;
    
    while (!q.empty()) {
        auto [cur_z, cur_r, cur_c] = q.front();
        q.pop();
        
        if (cur_z == 4 && cur_r == 4 && cur_c == 4) {
            return visited[4][4][4];
        }
        
        for (int i = 0; i < 6; i++) {
            int nz = cur_z + dz[i];
            int nr = cur_r + dr[i];
            int nc = cur_c + dc[i];
            
            if (nz >= 0 && nz < 5 && nr >= 0 && nr < 5 && nc >= 0 && nc < 5) {
                
                if (visited[nz][nr][nc] == -1 && (maze[nz][nr] & (1 << nc))) {
                    visited[nz][nr][nc] = visited[cur_z][cur_r][cur_c] + 1;
                    q.push({nz, nr, nc});
                }
            }
        }
    }
    return 999999; 
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int tmp[5][5];
    int next_tmp[5][5];
    
    for (int b = 0; b < 5; b++) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                cin >> tmp[i][j];
            }
        }
        
        for (int r = 0; r < 4; r++) {
            for (int i = 0; i < 5; i++) {
                int row_val = 0;
                for (int j = 0; j < 5; j++) {
                    if (tmp[i][j] == 1) {
                        row_val |= (1 << j);
                    }
                }
                rotated_boards[b][r][i] = row_val;
            }
            
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    next_tmp[j][4 - i] = tmp[i][j];
                }
            }
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    tmp[i][j] = next_tmp[i][j];
                }
            }
        }
    }
    
    int order[5] = {0, 1, 2, 3, 4};
    int answer = 999999;

    do {
   
        for (int rot = 0; rot < 1024; rot++) {
            int r_counts[5];
            int temp = rot;
            for (int i = 0; i < 5; i++) {
                r_counts[i] = temp % 4; 
                temp /= 4;
            }
            
            int maze[5][5];
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    maze[i][j] = rotated_boards[order[i]][r_counts[i]][j];
                }
            }
            
            if (!(maze[0][0] & (1 << 0)) || !(maze[4][4] & (1 << 4))) {
                continue;
            }
            
            int cur_ans = bfs(maze);
            
            if (cur_ans < answer) {
                answer = cur_ans;
                if (answer == 12) {
                    cout << 12 << "\n";
                    return 0; 
                }
            }
        }
    } while (next_permutation(order, order + 5)); 
    
    if (answer == 999999) {
        cout << -1 << "\n";
    } else {
        cout << answer << "\n";
    }
    
    return 0;
}