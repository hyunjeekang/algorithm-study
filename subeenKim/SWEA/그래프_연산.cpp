#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<bool> visited(1000001, false);

int main3() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int N, M, ans = 0;
		cin >> N >> M;

		fill(visited.begin(), visited.end(), false);

		queue<pair<int, int>> q;
		q.push({N, 0});

		while (!q.empty()) {
			pair<int, int> cur = q.front();
			int x = cur.first;
			int cnt = cur.second;
			q.pop();

			if (x == M) {
				ans = cnt;
				break;
			}

			if (x + 1 <= 1000000 && !visited[x+1]) {
				q.push({ x + 1, cnt + 1 });
				visited[x + 1] = true;
			}
			if (x - 1 > 0 && !visited[x-1]) {
				q.push({ x - 1, cnt + 1 });
				visited[x - 1] = true;
			}
			if (x * 2 <= 1000000 && !visited[x*2]) {
				q.push({ x * 2, cnt + 1 });
				visited[x * 2] = true;
			}
			if (x - 10 > 0 && !visited[x-10]) {
				q.push({ x - 10, cnt + 1 });
				visited[x - 10] = true;
			}
		}
		cout << '#' << tc << " " << ans << endl;
	}
	return 0;
}