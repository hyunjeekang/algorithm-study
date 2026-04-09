#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N, M;
int answer = -1;

void dfs(int idx, vector<int>& list) {
  if (list.size() == M) {
    int xor_sum = 0; 
    for (auto l : list) {
      xor_sum ^= l;
    }
    answer = max(answer, xor_sum);
    return;
  }

  for (int i = idx; i <= N; i++) {
    list.push_back(i);
    dfs(i + 1, list); 
    list.pop_back();
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  if (cin >> N >> M) {
    vector<int> arr;
    dfs(1, arr);
    cout << answer << "\n";
  }
  
  return 0;
}