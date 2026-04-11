#include<iostream>
#include<vector>
using namespace std;

int N;
vector<bool> visited(8, false);

void dfs(vector<int>& arr){
  if (arr.size() == N){
    for(auto n: arr){
      cout<<n<<" ";
    }
    cout<<"\n";
    return;
  }

  for(int i=1; i<=N; i++){
    if(visited[i] == false){
    visited[i] = true;
    arr.push_back(i);
    dfs(arr);
    arr.pop_back();
    visited[i] = false;
    }
  }
}

int main(){
  cin>>N;
  vector<int> arr;
  dfs(arr);
}