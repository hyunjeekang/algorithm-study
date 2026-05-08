#include <iostream>

using namespace std;

class Magnet {
private:
	int poles[8]; 
	int top;    

public:
	Magnet() : top(0) {}

	void set_pole(int index, int val) {
		poles[index] = val;
	}

	void rotate(int direction) {
		if (direction == 1) {
			top = (top + 7) % 8;
		}
		else {
			top = (top + 1) % 8;
		}
	}

	int get_target_pole() {
		return poles[top];
	}

	int get_right_pole() {
		return poles[(top + 2) % 8];
	}

	int get_left_pole() {
		return poles[(top + 6) % 8];
	}
};

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin >> T;

	for (int test_case = 1; test_case <= T; ++test_case) {
		int K;
		cin >> K;

		Magnet magnets[4];

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 8; j++) {
				int val;
				cin >> val;
				magnets[i].set_pole(j, val);
			}
		}

		for (int i = 0; i < K; i++) {
			int idx, direction;
			cin >> idx >> direction;
			idx--;

			int move[4] = { 0 };
			move[idx] = direction;

			for (int j = idx; j > 0; j--) {
				if (magnets[j].get_left_pole() != magnets[j - 1].get_right_pole()) {
					move[j - 1] = -move[j];
				}
				else break;
			}

			for (int j = idx; j < 3; j++) {
				if (magnets[j].get_right_pole() != magnets[j + 1].get_left_pole()) {
					move[j + 1] = -move[j];
				}
				else break;
			}

			for (int j = 0; j < 4; j++) {
				if (move[j] != 0) {
					magnets[j].rotate(move[j]);
				}
			}
		}

		int total = 0;
		for (int i = 0; i < 4; i++) {
			if (magnets[i].get_target_pole() == 1)
				total += (1 << i);
		}

		cout << "#" << test_case << " " << total << "\n";
	}
	return 0;
}