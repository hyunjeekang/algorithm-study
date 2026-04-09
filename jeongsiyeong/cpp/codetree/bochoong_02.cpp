#include<iostream>
#include<vector>
using namespace std;

int N,M;

void dfs(int idx, vector<int>& list){
  if (list.size() == M){
    for(auto l:list){
      cout<<l<<" ";
    }
    cout<<"\n";
    return;
  }

  for(int i=idx; i<=N; i++){
    list.push_back(i);
    dfs(i+1, list);
    list.pop_back();
  }
}

int main(){
  cin>>N>>M;
  vector<int> arr;
  dfs(1, arr);

}