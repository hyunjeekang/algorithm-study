#include<iostream>
#include<vector>
using namespace std;

struct Edge{
  int u, v, w;

  bool operator<(const Edge& other) const{
    return w < other.w;
  }
};

int parent_node[1005];

int find_parent(int x){
  if(parent_node[x] == x) return x;

  return parent_node[x] = find_parent(parent_node[x]);
}

void union_parent(int a, int b){
  a = find_parent(a);
  b = find_parent(b);

  if(a < b) parent_node[b] = a;
  else parent_node[a] = b;
 }

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int T;
  cin>>T;

  for(int test_case=1; test_case<=T; ++test_case){
    int V, E;
    cin>>V>>E;

    vector<Edge> edges(E);

    for(int i=0; i<E; i++){
      cin>>edges[i].u >> edges[i].v >> edges[i].w;
    }

    sort(edges.begin(), edges.end());

    for(int i=0; i<=V; ++i){
      parent_node[i] = i;
    }

    int total_weight = 0;
    int edge_count = 0;

    for(int i=0; i<E; i++){
      int u = edges[i].u;
      int v = edges[i].v;
      int w = edges[i].w;

      if(find_parent(u) != find_parent(v)){
        union_parent(u,v);
        total_weight += w;
        edge_count++;

        if(edge_count == V) break;
      }
    }
    cout<<"#"<<test_case<<" "<<total_weight<<"\n";
  }
  
  return 0;
}