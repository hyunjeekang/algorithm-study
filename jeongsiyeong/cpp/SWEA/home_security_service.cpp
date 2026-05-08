#include <iostream>
#include <cmath> // abs
using namespace std;

int COST[50];

int house_r[400];
int house_c[400];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    for (int k = 0; k < 50; k++) {
        COST[k] = k > 0 ? (k * k + (k - 1) * (k - 1)) : 0;
    }

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        int N, M;
        cin >> N >> M;

        int total_houses = 0;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                int a;
                cin >> a;
                if (a == 1) {
                    house_r[total_houses] = r;
                    house_c[total_houses] = c;
                    total_houses++;
                }
            }
        }

        int max_total_profit = total_houses * M;
        int max_houses = 0;
        bool found_absolute_max = false; 

        for (int r = 0; r < N; r++) {
            if (found_absolute_max) break;
            
            for (int c = 0; c < N; c++) {
                if (found_absolute_max) break;

                int dist_count[45] = {0, };
                int max_dist = 0; 
                
                for (int i = 0; i < total_houses; ++i) {
                    int dist = abs(r - house_r[i]) + abs(c - house_c[i]);
                    dist_count[dist]++;
                    if (dist > max_dist) max_dist = dist; 
                }

                int covered_houses = 0;

                for (int k = 1; k <= max_dist + 1; k++) {
                    covered_houses += dist_count[k - 1];

                    if (COST[k] > max_total_profit)
                        break;

                    if (covered_houses * M >= COST[k]) {
                        if (covered_houses > max_houses) {
                            max_houses = covered_houses;
                            
                            if (max_houses == total_houses) {
                                found_absolute_max = true;
                                break; 
                            }
                        }
                    }

                    if (covered_houses == total_houses) {
                        break;
                    }
                }
            }
        }
        cout << "#" << test_case << " " << max_houses << "\n";
    }

    return 0;
}