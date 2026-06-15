#include <iostream>
#include <string>
#include <set>
#include <iterator>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++) {
		int N, K;
		cin >> N >> K;

		string str;
		cin >> str;

		int L = N / 4;

		str += str.substr(0, L - 1);

		set<int, greater<int>> nums;

		for (int i = 0; i < N; i++) {
			string h_str = str.substr(i, L);

			int num = stoi(h_str, nullptr, 16);
			nums.insert(num);
		}

		auto it = nums.begin();
		advance(it, K - 1);

		cout << "#" << test_case << " " << *it << "\n";
	}
}