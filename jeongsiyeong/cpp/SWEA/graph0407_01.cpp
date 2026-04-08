#include<iostream>
#include<queue>
#include<vector>

const int INF = 9999999;

using namespace std;

int main(){
  int T;
  cin>>T;

  for(int test_case = 1; test_case<=T; ++test_case){
    int N, E;
    cin>>N>>E;

    vector<vector<pair<int, int>>> data(N+1);

    for (int i=0; i<E; i++){
      int s,e,w;
      cin>>s>>e>>w;
      data[s].push_back({w,e});
    }

    priority_queue<pair<int,int>, vector<pair<int, int>>, greater<pair<int,int>>> Q;
    Q.push({0,0});

    vector<int> distances(N+1,INF);
    distances[0] = 0;

    while (!Q.empty()){
      int curr_dist, curr_node;
      curr_dist = Q.top().first;
      curr_node = Q.top().second;
      Q.pop();
      
      if (distances[curr_node] < curr_dist){
        continue;
      } 

      for(auto p : data[curr_node]){
        int delta = p.first;
        int next_node = p.second;
        int next_dist = delta + curr_dist;

        if (next_dist < distances[next_node]){
          distances[next_node] = next_dist;
          Q.push({next_dist, next_node});
        }
      }
    }

    cout<<'#'<<test_case<<" "<<distances[N]<<"\n";
  }
  return 0;
}