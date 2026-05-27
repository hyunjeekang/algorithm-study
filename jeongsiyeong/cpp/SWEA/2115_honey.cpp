#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, C;
int board[10][10];
int profit[10][10]; 

void precalculate() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= N - M; j++) {
            int max_val = 0;
            
            for (int bit = 1; bit < (1 << M); bit++) {
                int current_sum = 0;
                int current_profit = 0;
                
                for (int k = 0; k < M; k++) {
                    if (bit & (1 << k)) {
                        current_sum += board[i][j + k];
                        current_profit += board[i][j + k] * board[i][j + k];
                    }
                }
                
                if (current_sum <= C) {
                    max_val = max(max_val, current_profit);
                }
            }
            profit[i][j] = max_val;
        }
    }
}

void solve() {
    cin >> N >> M >> C;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    precalculate();

    int ans = 0;
    
    for (int r1 = 0; r1 < N; r1++) {
        for (int c1 = 0; c1 <= N - M; c1++) {
            for (int r2 = r1; r2 < N; r2++) {
                int start_c2 = (r1 == r2) ? c1 + M : 0;
                
                for (int c2 = start_c2; c2 <= N - M; c2++) {
                    ans = max(ans, profit[r1][c1] + profit[r2][c2]);
                }
            }
        }
    }
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "#" << t << " ";
        solve();
    }
    return 0;
}