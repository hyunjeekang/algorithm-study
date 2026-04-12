#include<iostream>
#include<vector>
#include<queue>
#include<string>
using namespace std;

int dc[] = {1, 0, -1, 0};
int dr[] = {0, 1, 0, -1};
 
int main(){
  int T;
  cin>>T;

  for(int test_case=1; test_case<=T; ++test_case){
    int N;
    cin>>N;
    vector<vector<int>> arr(N, vector<int> (N));
    int start_r, start_c, goal_r, goal_c;

    for(int r=0; r<N; r++){
      string s;
      cin>>s;
      for(int c=0; c<N; c++){
        arr[r][c] = s[c] - '0';

        if(arr[r][c] == 2){
          start_r =r;
          start_c = c;
        }
        else if(arr[r][c] == 3){
          goal_r = r;
          goal_c = c;
        }
      }

      queue<pair<int,int>> q;
      q.push({start_r, start_c});
      vector<vector<int>> visited(N, vector<int>(N, -1));

      visited[start_r][start_c] = 0;

      while(!q.empty()){
        int cur_r, cur_c;
        cur_r = q.front().first;
        cur_c = q.front().second;

        if(cur_r == goal_r && cur_c == goal_c) break;

        for(int i=0; i<4; i++){
          int nr = cur_r +dr[i];
          int nc = cur_c + dc[i];

          if(nr>=0 && nr<N && nc>=0 && nc<N && visited[nr][nc] == -1 && arr[nr][nc] != 1){
              visited[nr][nc] = visited[cur_r][cur_c] + 1;
              q.push({nr, nc});
          }
        }
      }

      cout<<"#"<<test_case<<" "<<visited[goal_r][goal_c]<<"\n";
    }


  }
  return 0;
}