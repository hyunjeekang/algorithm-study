#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int get_stair_time(int* team_dists, int sz, int stair_len) {
    if (sz == 0) return 0;

    sort(team_dists, team_dists + sz);

    int q[10]; 
    int head = 0;
    int tail = 0;

    for (int i = 0; i < sz; i++) {
        int arrival_time = team_dists[i] + 1;

        if (tail - head < 3) {
            q[tail++] = arrival_time + stair_len;
        } 
        else {
            int prev_finish_time = q[head++];
            q[tail++] = max(arrival_time, prev_finish_time) + stair_len;
        }
    }
    return q[tail - 1]; 
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++) {
        int N;
        cin >> N;

        int persons[10][2];
        int p_idx = 0;

        int stairs[2][3];
        int s_idx = 0;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                int val;
                cin >> val;
                if (val == 1) {
                    persons[p_idx][0] = r;
                    persons[p_idx][1] = c;
                    p_idx++;
                } else if (val > 1) {
                    stairs[s_idx][0] = r;
                    stairs[s_idx][1] = c;
                    stairs[s_idx][2] = val;
                    s_idx++;
                }
            }
        }

        int dist[10][2];
        for (int i = 0; i < p_idx; i++) {
            dist[i][0] = abs(persons[i][0] - stairs[0][0]) + abs(persons[i][1] - stairs[0][1]);
            dist[i][1] = abs(persons[i][0] - stairs[1][0]) + abs(persons[i][1] - stairs[1][1]);
        }

        int answer = 1e9;
        int total_cases = 1 << p_idx;

        for (int mask = 0; mask < total_cases; mask++) {
            
            int team1[10]; int sz1 = 0;
            int team2[10]; int sz2 = 0;

            for (int i = 0; i < p_idx; i++) {
                if (mask & (1 << i)) {
                    team2[sz2++] = dist[i][1];
                } else {
                    team1[sz1++] = dist[i][0];
                }
            }

            int time1 = get_stair_time(team1, sz1, stairs[0][2]);
            int time2 = get_stair_time(team2, sz2, stairs[1][2]);

            int current_case_time = max(time1, time2);

            if (current_case_time < answer) {
                answer = current_case_time;
            }
        }

        cout << "#" << test_case << " " << answer << "\n";
    }
    
    return 0;
}