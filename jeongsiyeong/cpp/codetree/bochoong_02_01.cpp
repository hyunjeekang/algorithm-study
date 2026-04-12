#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<int> arr;
int max_xor = -1;

void dfs(int idx, int cnt, int current_xor) {
    if (cnt == M) {
        max_xor = max(max_xor, current_xor);
        return;
    }

    for (int i = idx; i < N; i++) {
        dfs(i + 1, cnt + 1, current_xor ^ arr[i]);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (cin >> N >> M) {
        arr.resize(N);
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }

        dfs(0, 0, 0);

        cout << max_xor << "\n";
    }

    return 0;
}