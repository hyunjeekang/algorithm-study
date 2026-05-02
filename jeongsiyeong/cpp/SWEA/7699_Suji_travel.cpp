#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int dr[4] = { 1, 0, -1, 0 };
int dc[4] = { 0, 1, 0, -1 };
int R, C;

void dfs(int& answer, int cur_r, int cur_c, int count, vector<bool>& alpha_visited, const vector<string>& grid) {
	if (answer < count) {
		answer = count;
	}

	for (int i = 0; i < 4; i++) {
		int nr = cur_r + dr[i];
		int nc = cur_c + dc[i];

		if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
			int next_alpha = grid[nr][nc] - 'A'; 

			if (!alpha_visited[next_alpha]) {
				alpha_visited[next_alpha] = true;
				dfs(answer, nr, nc, count + 1, alpha_visited, grid); 
				alpha_visited[next_alpha] = false;    
			}
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {
		cin >> R >> C;

		vector<string> grid(R);
		for (int i = 0; i < R; i++) {
			cin >> grid[i];
		}

		vector<bool> alpha_visited(26, false); 
		int answer = 0;

		int start_alpha = grid[0][0] - 'A';
		alpha_visited[start_alpha] = true;

		dfs(answer, 0, 0, 1, alpha_visited, grid);

		cout << "#" << test_case << " " << answer << "\n";
	}

	return 0;
}