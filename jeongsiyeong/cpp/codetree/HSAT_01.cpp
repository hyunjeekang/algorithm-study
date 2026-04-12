#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node{
  int r, c, dir, time;
};

int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

int req_dir[13] = {0, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3,2,1};
int allowed_dirs[13] = {0, 11, 13,14,7,9,12,6,3,3,9,12,6};

bool visited[105][105][4][4];
bool unique_cells[105][105];

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N,T;
  cin >> N >> T;

  vector<vector<vector<int>>> signals(N, vector<vector<int>>(N, vector<int>(4)));
  for(int i=0; i<N; i++){
    for(int j=0; j<N; j++){
      for(int k=0; k<4; k++){
        cin >> signals[i][j][k];
      }
    }
  }

  queue<Node> q;
  q.push({0, 0, 3, 0});
  visited[0][0][3][0] = true;

  unique_cells[0][0] = true;
  int ans = 1;

  while(!q.empty()){
    Node cur = q.front();
    q.pop();

    if (cur.time == T) continue;

    int sig_id = signals[cur.r][cur.c][cur.time % 4];
    int req = req_dir[sig_id];
    int allowed = allowed_dirs[sig_id];

    if( cur.dir == req){
      for(int i=0; i<4; i++){
        if(allowed & (1<<i)){
          int nr = cur.r + dr[i];
          int nc = cur.c + dc[i];

          if (nr >= 0 && nr < N && nc >= 0 && nc <N){
            int next_mod = (cur.time + 1) % 4;
            if (!visited[nr][nc][i][next_mod]){
              visited[nr][nc][i][next_mod] = true;

              if (!unique_cells[nr][nc]){
                unique_cells[nr][nc] = true;
                ans++;
              }
              q.push({nr, nc, i, cur.time+1});
            }
          }
        }
      }
    }
  }

  cout << ans<<"\n";
  return 0;
}

