#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<tuple>
using namespace std;

int get_dist(int sr, int sc, int pr, int pc) {
	return abs(pr - sr) + abs(pc - sc);
}

int get_stair_time(vector<int>& team_dists, int stair_len) {
	if (team_dists.empty()) {
		return 0;
	}

	sort(team_dists.begin(), team_dists.end());

	queue<int> q;

	for (int dist : team_dists) {
		int arrival_time = dist + 1;

		if (q.size() < 3) {
			q.push(arrival_time + stair_len);
		}
		else {
			int prev_finish_time = q.front();
			q.pop();
			q.push(max(arrival_time, prev_finish_time) + stair_len);
		}
	}
	return q.back();
}

int main() {
	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {
		int N;
		cin >> N;

		vector<pair<int, int>> persons;
		vector<tuple<int, int, int>> stairs;

		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				int a;
				cin >> a;
				if (a == 1) {
					persons.push_back({ r, c });
				}
				else if(a > 1) {
					stairs.push_back(make_tuple( r, c, a ));
				}
			}
		}

		int num_persons = persons.size();
		int answer = 1e9;

		for (int mask = 0; mask < (1 << num_persons); mask++) {
			vector<int> team1_dists;
			vector<int> team2_dists;
			int sr1, sc1, slen1;
			int sr2, sc2, slen2;
			tie(sr1, sc1, slen1) = stairs[0];
			tie(sr2, sc2, slen2) = stairs[1];
			for (int i = 0; i < num_persons; i++) {
				int pr = persons[i].first;
				int pc = persons[i].second;
				
				if (mask & (1 << i)) {
					team2_dists.push_back(get_dist(sr2, sc2, pr, pc));
				}
				else {
					team1_dists.push_back(get_dist(sr1, sc1, pr, pc));
				}
			}
			int time1 = get_stair_time(team1_dists, slen1);
			int time2 = get_stair_time(team2_dists, slen2);

			int current_case_time = max(time1, time2);

			answer = min(answer, current_case_time);
		}
		cout << "#" << test_case << " " << answer << "\n";
	}
}