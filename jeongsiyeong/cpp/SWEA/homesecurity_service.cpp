#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
 
using namespace std;
 
int COSTS[50];
int dist_count[50];
pair<int, int> houses[400]; 
 
void precompute_costs() {
    for (int k = 1; k < 50; ++k) {
        COSTS[k] = k * k + (k - 1) * (k - 1);
    }
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    precompute_costs();
 
    int T;
    if (!(cin >> T)) return 0;
 
    for (int test_case = 1; test_case <= T; ++test_case) {
        int N, M;
        cin >> N >> M;
 
        int house_cnt = 0;
         
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                int val;
                cin >> val;
                if (val == 1) {
                    houses[house_cnt++] = {r, c};
                }
            }
        }
 
        int max_total_profit = house_cnt * M;
        int max_houses = 0;
 
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                memset(dist_count, 0, sizeof(dist_count));
 
                for (int i = 0; i < house_cnt; ++i) {
                    int dist = abs(r - houses[i].first) + abs(c - houses[i].second);
                    dist_count[dist]++;
                }
 
                int covered_houses = 0;
                for (int k = 1; k <= 2 * N + 1; ++k) {
                    covered_houses += dist_count[k - 1];
 
                    if (COSTS[k] > max_total_profit) break; 
                     
                    if (covered_houses <= max_houses) continue;
 
                    if (covered_houses * M >= COSTS[k]) {
                        max_houses = covered_houses;
                    }
                }
            }
        }
 
        cout << "#" << test_case << " " << max_houses << "\n";
    }
 
    return 0;
}