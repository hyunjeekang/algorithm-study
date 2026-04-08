#include <iostream>
#include <vector>
using namespace std;

int n, k;

void dfs(vector<int> &cur_list) {
    if (cur_list.size() == k) {
        for (int i = 0; i < k; i++) {
            cout << cur_list[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 1; i <= n; i++) {
        int sz = cur_list.size();
        if (sz >= 2 && cur_list[sz - 1] == i && cur_list[sz - 2] == i) {
            continue;
        }

        cur_list.push_back(i);
        dfs(cur_list);
        cur_list.pop_back(); 
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k; 
    vector<int> arr;
    dfs(arr);
    
    return 0;
}