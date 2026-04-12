#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };
int arr[1000][1000];
int main2() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int first = 1000001, max_num = -1, N;
		cin >> N;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> arr[i][j];
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int cnt = 1, x=i, y=j;

				while (true) {
					bool is_found = false;
					for (int d = 0; d < 4; d++) {
						int nx = x + dx[d];
						int ny = y + dy[d];

						if (((0 <= nx && nx < N) && (0 <= ny && ny < N)) && (arr[nx][ny] == arr[x][y] + 1)) {
							cnt ++;
							x = nx;
							y = ny;
							is_found = true;
							break;
						}
					}
					if (!is_found) {
						break;
					}
				}
				if (cnt > max_num) {
					max_num = cnt;
					first = arr[i][j];
				}
				else if (cnt == max_num && first > arr[i][j]) {
					first = arr[i][j];
				}
			}
		}

		cout << '#' << tc << " " << first << " " << max_num << endl;
	}
	return 0;
}