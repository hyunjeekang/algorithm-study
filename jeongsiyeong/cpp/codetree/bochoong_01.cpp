#include <iostream>
#include <vector>
using namespace std;

int N;
int cnt = 0;

void dfs(vector<int>& cur_list){
    if(cur_list.size() == N){
        cnt+=1;
        return;
    }
    if(cur_list.size() > N){
        return;
    }

    for(int k=1; k<=4; k++){
        vector<int> new_list;
        new_list.assign(cur_list.begin(), cur_list.end());
        for(int i=0; i<k; i++){
            new_list.push_back(k);
        }
        dfs(new_list);
    }
}


int main() {
    cin >> N;
    vector<int> arr;
    dfs(arr);
    cout<<cnt<<"\n";
    // Please write your code here.
    return 0;
}