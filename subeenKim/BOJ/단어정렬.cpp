#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const string& a, const string& b) {
	if (a.length() != b.length()) {
		return a.length() < b.length();
	}
	return a < b;
}
int main() {
	int N;
	cin >> N;
	set<string> s;
	string str;
	for (int i = 0;i < N;i++) {
		cin >> str;
		s.insert(str);
	}

	// set을 쓰지 않고 vector로 바로 하려면
	// unique, erase 활용 가능!
	// v.erase(unique(v.begin(). v.end)), v.end());

	vector<string> v(s.begin(), s.end());
	sort(v.begin(), v.end(), compare);

	for (string word : v) {
		cout << word << "\n";
	}
}