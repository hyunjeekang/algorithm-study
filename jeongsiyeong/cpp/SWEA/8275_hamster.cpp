#include <iostream>
 
using namespace std;
 
int N, X, M;
int l_cond[10], r_cond[10], s_cond[10];
int cages[10];
int psum[10];      
int best_cages[10];
int max_sum = -1;
 
void find_case(int idx, int current_sum) {
    if (idx > 0) {
        psum[idx] = psum[idx - 1] + cages[idx]; 
         
        for (int i = 0; i < M; ++i) {
            if (l_cond[i] <= idx) {
                int part_sum = psum[idx] - psum[l_cond[i] - 1]; 
                 
                if (r_cond[i] == idx) {
                    if (part_sum != s_cond[i]) return; 
                } else if (r_cond[i] > idx) {
                    if (part_sum > s_cond[i]) return; 
                }
            }
        }
    }
 
    if (idx < N && current_sum + (N - idx) * X <= max_sum) {
        return;
    }
 
    if (idx == N) {
        if (max_sum < current_sum) {
            max_sum = current_sum;
            for (int i = 1; i <= N; ++i) {
                best_cages[i] = cages[i];
            }
        }
        return;
    }
 
    for (int i = 0; i <= X; ++i) {
        cages[idx + 1] = i;
        find_case(idx + 1, current_sum + i);
    }
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    int T;
    cin >> T;
 
    for (int test_case = 1; test_case <= T; ++test_case) {
        cin >> N >> X >> M;
 
        max_sum = -1;
        for (int i = 0; i < M; ++i) {
            cin >> l_cond[i] >> r_cond[i] >> s_cond[i];
        }
 
        psum[0] = 0; 
         
        find_case(0, 0);
 
        cout << "#" << test_case << " ";
        if (max_sum == -1) {
            cout << "-1\n";
        } else {
            for (int i = 1; i <= N; ++i) {
                cout << best_cages[i] << (i == N ? "" : " ");
            }
            cout << "\n";
        }
    }
     
    return 0;
}