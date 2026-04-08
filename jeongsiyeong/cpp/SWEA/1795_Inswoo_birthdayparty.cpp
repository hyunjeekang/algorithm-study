#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 1e9;
vector<pair<int,int>> adj[1001];
vector<pair<int,int>> reverse_adj[1001];

void dijkstra(int start, int dist[], vector<pair<int,int>> graph[]){
  priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
  dist[start] = 0;
  pq.push({0, start});

  while(!pq.empty()){
    int d = pq.top().first;
    int curr = pq.top().second;
    pq.pop();

    if(dist[curr] < d) continue;

    for(auto& edge : graph[curr]){
      int next = edge.first;
      int next_dist = d + edge.second;
      if(next_dist < dist[next]){
        dist[next] = next_dist;
        pq.push({next_dist, next});
      }
    }
  }
}

int main(){
  int T;
  cin>>T;

  for(int test_case=1; test_case<=T; ++test_case){
    for(int i=1; i<=1000; i++) {
        adj[i].clear();
        reverse_adj[i].clear();
    }

    int N,M,X;
    cin>>N>>M>>X;

    for(int i=0; i<M; i++){
      int x,y,c;
      cin>>x>>y>>c;

      adj[x].push_back({y, c});
      reverse_adj[y].push_back({x,c});
    }

    int dist_to_X[1001], dist_from_X[1001];
    fill(dist_to_X, dist_to_X + 1001, INF);
    fill(dist_from_X, dist_from_X + 1001, INF);
    dijkstra(X, dist_to_X, reverse_adj);
    dijkstra(X, dist_from_X, adj);

    int max_time = 0;
    for (int i=1; i<=N; i++){
      if(dist_to_X[i] != INF && dist_from_X[i]!=INF){
        max_time = max(max_time, dist_to_X[i] + dist_from_X[i]);
      }
    }
    cout<<"#"<<test_case<<" "<<max_time<<"\n";
  }
}