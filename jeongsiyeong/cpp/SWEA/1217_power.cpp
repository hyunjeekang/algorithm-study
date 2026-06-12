#include <iostream>

using namespace std;

long long power(long long base, long long exp) {
	long long result = 1;

	while (exp > 0) {
		if (exp & 1) {
			result *= base;
		}

		base *= base;

		exp >>= 1;


	}

	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T = 10;
	for (int test_case = 1; test_case <= T; ++test_case) {
		int tc;
		cin >> tc;

		int N, M;
		cin >> N >> M;

		cout << "#" << test_case << " " << power(N, M) << "\n";
	}
}